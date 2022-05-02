from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    text = models.TextField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]

