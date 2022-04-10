from django.db import models
from main.models import User

# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    image = models.ImageField(default="default.jpg", upload_to="course_pics")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    availability = models.BooleanField(default=True)
    url = models.CharField(max_length=255, default="\\course\\")
    difficulty = models.CharField(
        max_length=12,
        choices=(
            ("Beginner", "Beginner"),
            ("Intermediate", "Intermediate"),
            ("Advanced", "Advanced"),
        ),
        default="Beginner",
    )

    def __str__(self):
        return self.name
