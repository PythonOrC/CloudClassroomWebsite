from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path(
        "signin/",
        auth_views.LoginView.as_view(template_name="signin.html"),
        name="signin",
    ),
    path(
        "signout/",
        auth_views.LogoutView.as_view(template_name="signout.html"),
        name="signout",
    ),
    path("<str:place>/", views.general, name="general"),
]
