from django.db import models


# Create your models here.
class Task(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return f"{self.text}"
