from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "course"

urlpatterns = [
    path("", views.course, name="course"),
    path("all/", views.all_courses, name="all"),
    path("<str:url>/", views.view_course, name="view_course"),
]
