from django.urls import path
from .views import login_user, check_login, logout_user

urlpatterns = [
    path("", login_user, name = "index"),
    path("home/", check_login, name="home"),
    path("logout/", logout_user, name="logout")
]
