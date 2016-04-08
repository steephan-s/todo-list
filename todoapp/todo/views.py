from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .models import Task
from django.template import loader
from django.core.urlresolvers import reverse

def index(request):
    todo_list = Task.objects.all().order_by('add_date')
    context = {'todo_list': todo_list}
    return render(request, 'todo/index.html', context)
    
    def __str__(self):
        return self.todo_text

def push_function(request):
    if request.method == "POST":
        temp_task = request.POST.get("task_field", "")
        temp_date = request.POST.get("date_field", "")
        push_data = Task(todo_text=temp_task, add_date=temp_date)
        push_data.save()
        return HttpResponseRedirect(reverse('todo:index'))


