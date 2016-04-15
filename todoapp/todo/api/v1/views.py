from todo.models import Task
from todo.serializers import TaskSerializer
from rest_framework import generics

class index(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
