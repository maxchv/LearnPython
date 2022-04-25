from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True)
    post = models.ForeignKey('Post', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.text[:20]


class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField()
    draft = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated']
