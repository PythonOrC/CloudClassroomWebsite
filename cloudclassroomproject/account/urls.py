from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "account"

urlpatterns = [
    path("", views.account_overview, name="account_overview"),
]
