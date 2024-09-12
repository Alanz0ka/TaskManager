from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

class TaskAPIView(APIView):

    def get(self, request):
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)