from django.contrib.auth.models import User
from django.db import models


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.user.username


class Course(models.Model):
    name = models.CharField(max_length=50, null=False)
    start = models.DateField()
    end = models.DateField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.name
