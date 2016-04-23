from todo.models import Task
from todo.serializers import TaskSerializer
from rest_framework import generics
from django.shortcuts import render

class index(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

def detail(request):
     return render(request, 'todo/detail.html')
