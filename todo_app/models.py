from django.db import models
from django.urls import reverse
# Create your models here.

#from todo_app.models import Tod o


class Todo(models.Model):
    day = models.CharField(max_length=25)
    deadline = models.DateField()
    task = models.TextField()

    def __str__(self):
        return f'Планы на {self.day}'

    def get_url(self):
        return reverse('one-day', args=[self.id])
