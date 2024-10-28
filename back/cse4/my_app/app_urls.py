from django.urls import path
from .views import read_view, login_view

urlpatterns = [
    path("read/", read_view, name="read"),
    path("", login_view, name="login")
]

# app_urls.py