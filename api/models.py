from pyexpat import model
from unicodedata import name
from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    email = models.EmailField()
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-createdAt']

    def __str__(self):
        return self.name
        