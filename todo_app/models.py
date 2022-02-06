from django.db import models
from django.urls import reverse
# Create your models here.

#from todo_app.models import Tod o


class Todo(models.Model):
    day = models.CharField(max_length=25, verbose_name='День недели')
    date = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    task = models.TextField(verbose_name='Задачи на день')

    class Meta:
        verbose_name = 'Заметку'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return f'Планы на {self.day}'

    def get_url(self):
        return reverse('one-day', args=[self.id])
