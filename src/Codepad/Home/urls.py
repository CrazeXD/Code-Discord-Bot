from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_rq, name="login"),
    path("home/", views.dashboard, name="home"),
]