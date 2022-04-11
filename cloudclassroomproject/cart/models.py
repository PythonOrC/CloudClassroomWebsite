from django.db import models
from main.models import UserProfile
from course.models import Course

# Create your models here.
# class OrderItem(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
#     user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
#     is_ordered = models.BooleanField(default=False)
#     date_added = models.DateTimeField(auto_now=True)
#     date_ordered = models.DateTimeField(null=True)

#     def __str__(self):
#         return self.course.name


class Order(models.Model):
    ref_code = models.CharField(max_length=20, default = '')
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, blank=True, related_name="course", on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_profile.user.username}'s order of {str(self.course)}"
