from django.db import models
from django.utils.timezone import localtime

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        formatted_date = localtime(self.due_date).strftime("%d/%m/%Y %H:%M:%S")
        return f"{
            self.title} - {self.description} - {formatted_date}"
