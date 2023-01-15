from django.db import models

# Create your models here.

# Create your models here.
class Zoom(models.Model):
    id = models.AutoField(primary_key=True)
    meeting_id = models.CharField(max_length=255)
    meeting_password = models.CharField(max_length=255)
    meeting_link = models.CharField(max_length=255)

    def __str__(self):
        return "id: " + self.meeting_id
