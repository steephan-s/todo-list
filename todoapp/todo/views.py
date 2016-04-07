from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
from django.template import loader


def index(request):
    todo_list = Task.objects.all()
    context = {'todo_list': todo_list}
    return render(request, 'todo/index.html', context)




