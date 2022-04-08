from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path(
        "signin/",
        auth_views.LoginView.as_view(template_name="main/signin.html"),
        name="signin",
    ),
    path(
        "signout/",
        auth_views.LogoutView.as_view(template_name="main/signout.html"),
        name="signout",
    ),
    # path("profile/", views.profile, name="profile"),
    path("courses-all/", views.all_courses, name="all_courses"),
    path("course/<str:url>/", views.view_course, name="view_course"),
    path("<str:place>/", views.general, name="general"),
]
