from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    courses = models.ManyToManyField("account.MyCourse", blank=True)
    # cart = models.ManyToManyField("course.Course", blank=True, related_name="cart")

    def __str__(self):
        return f"{self.user.username} Profile"
