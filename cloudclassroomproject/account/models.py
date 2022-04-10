from django.db import models

# Create your models here.


class MyCourse(models.Model):
    course = models.ForeignKey("course.Course", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.course.name

