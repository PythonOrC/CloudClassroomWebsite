from django.db import models
from main.models import UserProfile
from course.models import Course
from main.models import UserProfile

# Create your models here.
class OrderItem(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.course.name


class Order(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    ref_code = models.CharField(max_length=20, default = '')
    items = models.ManyToManyField(OrderItem)
    is_ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_profile.user.username

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.course.price for item in self.items.all()])
