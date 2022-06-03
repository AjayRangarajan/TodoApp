from .models import Task
from .serielizers import TaskSerielizer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Home(APIView):

    def get(self, request):
            api_urls = {
                'List of endpoints': '/task/',
                'List Tasks': '/task/all/',
                'Add new Tasks': '/task/new/',
            }
            return Response(api_urls)

class ViewTasks(APIView):

    def get(self, request):
        tasks = Task.objects.all()
        serielizer = TaskSerielizer(tasks, many=True)
        return Response(serielizer.data)

class AddTask(APIView):

    def post(self, request):
        serielizer = TaskSerielizer(data=request.data)

        if serielizer.is_valid():
            serielizer.save()
            return Response(serielizer.data, status=status.HTTP_201_CREATED)
        return Response(serielizer.errors, status=status.HTTP_400_BAD_REQUEST)