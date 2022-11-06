from django.db import models
from django.conf import settings


class Task(models.Model):
    topic = models.CharField(verbose_name='Тема', max_length=100, blank=True)
    title = models.CharField(verbose_name='Заголовок задачи', max_length=255)
    task_text = models.TextField(verbose_name='Формулировка задачи')
    closed = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='task')

    def __str__(self):
        return f'Username: {self.user.username} | {self.title}'
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'