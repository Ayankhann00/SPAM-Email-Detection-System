from django.contrib import admin
from django.urls import path
from spam_app import views  # import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # main page
]
