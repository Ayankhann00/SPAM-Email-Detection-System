import os
import joblib
from django.conf import settings
from django.shortcuts import render

# Paths to ML models
NAIVE_BAYES_MODEL = os.path.join(settings.BASE_DIR, "spam_app", "ml_models", "naive_bayes.pkl")
VECTORIZER = os.path.join(settings.BASE_DIR, "spam_app", "ml_models", "vectorizer.pkl")



# Load models into memory (only once)
classifier_nb = joblib.load(NAIVE_BAYES_MODEL)
vectorizer_nb = joblib.load(VECTORIZER)



def home(request):
    prediction = None
    email_text = ""
    algorithm = "naive_bayes"  # default

    if request.method == "POST":
        email_text = request.POST.get("email_text", "")
        algorithm = request.POST.get("algorithm", "naive_bayes")

        if email_text:
            if algorithm == "naive_bayes":
                X = vectorizer_nb.transform([email_text]).toarray()
                result = classifier_nb.predict(X)[0]
            elif algorithm == "svm" and classifier_svm and vectorizer_svm:
                X = vectorizer_svm.transform([email_text]).toarray()
                result = classifier_svm.predict(X)[0]
            else:
                result = 0  # Default: Not Spam if model missing

            prediction = "Spam" if result == 1 else "Not Spam"

    return render(request, "index.html", {
        "prediction": prediction,
        "email_text": email_text,
        "algorithm": algorithm
    })
