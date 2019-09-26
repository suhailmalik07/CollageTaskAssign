from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse


class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('home')

class Task(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student', limit_choices_to={'is_student':True})
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    task_image = models.ImageField(upload_to='profile_pics', null=False, blank=True)
    is_completed = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher')
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task', args=[self.pk])
        