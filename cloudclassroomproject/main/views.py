from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from cart.views import get_user_pending_order
# Create your views here.


def index(request):
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")

            messages.success(request, f"New account created: {username}")
            return redirect("signin")
        else:
            messages.error(request, "Invalid form")
    else:
        form = UserRegisterForm()
    return render(request, "signup.html", {"form": form})


def cart(request):
    order = get_user_pending_order(request)
    return render(request, "cart.html", {"order": order})


def general(request, place):
    restricted_places = ["profile"]
    if place in restricted_places and not request.user.is_authenticated:
        messages.error(request, "Please login to access this page")
        return redirect("main:signin")
    return render(request, f"{place}.html")
