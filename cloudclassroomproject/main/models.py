from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    courses = models.CharField(max_length=65535, default="")

    def __str__(self):
        return f"{self.user.username} Profile"


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    image = models.ImageField(default="default.jpg", upload_to="course_pics")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    availability = models.BooleanField(default=True)
    url = models.CharField(max_length=255, default="\\course\\")
    difficulty = models.CharField(max_length=255, default="Beginner")

    def __str__(self):
        return self.name
