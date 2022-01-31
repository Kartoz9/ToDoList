from django.db import models
from django.urls import reverse
# Create your models here.

#from todo_app.models import Tod o


class Todo(models.Model):
    day = models.CharField(max_length=25)
    number = models.IntegerField()
    month = models.IntegerField()
    task = models.CharField(max_length=200)

    def __str__(self):
        return f'Планы на {self.day} ({self.number}.{self.month})'

    def get_url(self):
        return reverse('one-day', args=[self.day])
