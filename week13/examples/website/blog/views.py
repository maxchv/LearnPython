from django.shortcuts import render
from .models import Post, Category, Tag


def index(request):
    posts = Post.objects.all()
    return render(request, "blog/index.html", {"posts": posts})


def post(request):
    return render(request, "blog/post.html")


