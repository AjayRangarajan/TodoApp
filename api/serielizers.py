from dataclasses import fields
from pyexpat import model
from .models import Task
from rest_framework import serializers

class TaskSerielizer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'