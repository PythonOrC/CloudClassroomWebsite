from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "cart"

urlpatterns = [
    path("<int:course_id>/", views.add_to_cart, name="add_to_cart"),
]
