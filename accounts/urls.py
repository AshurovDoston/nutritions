from django.urls import path
from .views import signup_view

urlpatterns = [
    # Signup page - /accounts/signup/
    path("signup/", signup_view, name="signup"),
]