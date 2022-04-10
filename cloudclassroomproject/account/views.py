from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="main:signin")
def account_overview(request):
    courses = request.user.userprofile.courses.all()
    return render(request, "profile.html", {"courses": courses})
