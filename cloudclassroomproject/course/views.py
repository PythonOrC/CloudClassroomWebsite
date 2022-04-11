from django.shortcuts import render
from .models import Course

# Create your views here.


def course(request):
    return render(request, "courses.html")


def all_courses(request):
    courses = Course.objects.all()
    return render(request, "courses-all.html", {"courses": courses})


def view_course(request, id):
    course = Course.objects.get(id=id)
    name = course.name
    context = {"course": course}
    return render(request, f"course-detail.html", context)
