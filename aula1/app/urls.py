from django.urls import path
from .views import login_user, check_login

urlpatterns = [
    path("", login_user, name = "index"),
    path("home/", check_login, name="home")
]
