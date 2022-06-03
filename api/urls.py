from django.urls import path
from .views import Home, ViewTasks, AddTask

urlpatterns = [
    path('', Home.as_view()),
    path('all/', ViewTasks.as_view()),
    path('new/', AddTask.as_view()),
]
