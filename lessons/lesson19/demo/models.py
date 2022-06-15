from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:20]
