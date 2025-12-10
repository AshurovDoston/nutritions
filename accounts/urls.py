from django.urls import path
from .views import account_view, current_datetime_view

urlpatterns = [
    path("", account_view, name="home"),
    path("time/", current_datetime_view, name="current_datetime"),
]