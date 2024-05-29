from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Todo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Власник нотаток', blank=True, null=True)
    day = models.CharField(max_length=100, verbose_name='День тижня (Наприклад: Понеділок (21.02))')
    date = models.DateTimeField(auto_now=True, verbose_name='Дата останньої змінни')
    task = models.TextField(verbose_name='Задачі на день')

    class Meta:
        verbose_name = 'Нотатку'
        verbose_name_plural = 'Нотатки'

    def __str__(self):
        return f'Задачі на {self.day}'

    def get_url(self):
        return reverse('one-day', args=[self.id])
