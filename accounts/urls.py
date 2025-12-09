from django.urls import path
from .views import home_view, current_datetime_view

urlpatterns = [
    path("", home_view, name="home"),
    path("time/", current_datetime_view, name="current_datetime"),
]