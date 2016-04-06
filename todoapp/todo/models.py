from django.db import models


class Task(models.Model):
    todo_text = models.CharField(max_length=200)
    add_date = models.DateTimeField('date added')
