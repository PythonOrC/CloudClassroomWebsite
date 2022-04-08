from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import UserProfile, Course

# Create your views here.


def index(request):
    return render(request, "main/index.html")


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
    return render(request, "main/signup.html", {"form": form})


def all_courses(request):
    courses = Course.objects.all()
    return render(request, "main/courses-all.html", {"courses": courses})


def view_course(request, url):
    return render(request, f"main/course/{url}.html")


def general(request, place):
    restricted_places = ["profile"]
    if place in restricted_places and not request.user.is_authenticated:
        messages.error(request, "Please login to access this page")
        return redirect("signin")
    return render(request, f"main/{place}.html")
