from django.db import models
from django.contrib.auth.models import User

class TaskList(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # vlasnik liste
    shared_with = models.ManyToManyField(User, related_name='shared_lists', blank=True)  # dijeljenje s drugim korisnicima

    def __str__(self):
        return self.name

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    deadline = models.DateField(null=True, blank=True)
    list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return self.title
