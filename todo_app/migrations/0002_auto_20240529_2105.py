# Generated by Django 3.2 on 2024-05-29 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name': 'Нотатку', 'verbose_name_plural': 'Нотатки'},
        ),
        migrations.AlterField(
            model_name='todo',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Власник нотаток'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата останньої змінни'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='day',
            field=models.CharField(max_length=100, verbose_name='День тижня (Наприклад: Понеділок (21.02))'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='task',
            field=models.TextField(verbose_name='Задачі на день'),
        ),
    ]