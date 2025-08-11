# Spam Email Detection System

![Spam Detection](https://img.shields.io/badge/Status-Complete-success)

A full-stack web application built with **Django** that detects whether an email or text message is spam or not using a **Naive Bayes machine learning model** with **Natural Language Processing (NLP)** techniques.

---

## 🚀 Project Overview

This system allows users to input an email or message text and classify it as **Spam** or **Not Spam**. The backend is powered by Django, while the machine learning model uses NLP to analyze the text and make predictions based on training data.

---

## Features

- User-friendly web interface built with Django and Bootstrap.
- Spam detection using a trained Naive Bayes classifier.
- NLP text vectorization for accurate prediction.
- Selection of algorithms for flexibility (currently supports Naive Bayes, expandable).
- Real-time result display with clean UI and responsive design.

---


---

## 📁 Project Structure

spam-email-detection-system/
│
├── spam_app/ # Django app
│ ├── ml_models/ # Saved ML models (naive_bayes.pkl, vectorizer.pkl)
│ ├── templates/ # HTML templates
│ ├── static/ # CSS, JS, assets
│ ├── views.py # Django views with model inference
│ └── ...
├── manage.py # Django management script
├── requirements.txt # Project dependencies
└── README.md # Project documentation

---

## 💻 Technologies Used

- Python 3.x
- Django Web Framework
- scikit-learn (for ML model)
- joblib (for model serialization)
- Natural Language Toolkit (NLTK) / or any other NLP tools used
- Bootstrap 5 (for responsive UI)

---

## 🛠 Installation & Setup

1. **Clone the repo**

```bash
git clone https://github.com/Ayankhann00/SPAM-Email-Detection-System.git
cd SPAM-Email-Detection-System
Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies
pip install -r requirements.txt
Run migrations
python manage.py migrate
Run the development server
python manage.py runserver
Open your browser
Navigate to http://127.0.0.1:8000 to use the app.
🔍 How It Works
User enters email or message text in the form.
The text is vectorized using a pre-trained vectorizer.
The Naive Bayes classifier predicts if the text is spam or not.
Result is displayed immediately on the web page.
📂 ML Model Training
(Optional if you want to share your training code)
You can train your own Naive Bayes spam classifier using:

Dataset: (e.g., SMS Spam Collection dataset)
Preprocessing text with tokenization, stopword removal, etc.
Using CountVectorizer or TfidfVectorizer from scikit-learn.
Train a Naive Bayes model and save it using joblib.
Contributions
Contributions, issues, and feature requests are welcome!
Feel free to check issues page.
License
This project is licensed under the MIT License. See the LICENSE file for details.
🙏 Acknowledgments
Special thanks to Arch Technologies for providing this internship opportunity and guidance.
Thanks to open-source libraries: Django, scikit-learn, Bootstrap, etc.
Contact
Ayan Khan
GitHub: Ayankhann00
<img width="1280" height="800" alt="Screenshot 2025-08-11 at 2 58 24 PM" src="https://github.com/user-attachments/assets/af21efc9-d742-4d3b-ad2e-3d33197a408a" />


