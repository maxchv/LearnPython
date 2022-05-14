from django.contrib.auth.models import User
from django.db.models import Model, CASCADE, CharField, TextField, DateTimeField, ForeignKey


class Post(Model):
    title = CharField(max_length=100, blank=False, null=False)
    text = TextField()
    created = DateTimeField(auto_now_add=True)
    modified = DateTimeField(auto_now=True)


class Comment(Model):
    post = ForeignKey(Post, related_name='comments', on_delete=CASCADE)
    user = ForeignKey(User, on_delete=CASCADE)
    text = TextField()
    created = DateTimeField(auto_now_add=True)
