from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Blog(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} [{self.author}]'


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
