from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Todo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец заметок', blank=True, null=True)
    day = models.CharField(max_length=100, verbose_name='День недели (Например: Понедельник (21.02))')
    date = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    task = models.TextField(verbose_name='Задачи на день')

    class Meta:
        verbose_name = 'Заметку'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return f'Планы на {self.day}'

    def get_url(self):
        return reverse('one-day', args=[self.id])
