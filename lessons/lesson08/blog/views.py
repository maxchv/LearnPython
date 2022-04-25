from django.shortcuts import render

from .forms import PostForm


def index(request):
    return render(request, 'blog/index.html')


def post(request, pk):
    return render(request, 'blog/post.html')


def create(request):
    context = {
        "form": PostForm()
    }
    return render(request, "blog/create_post.html", context)
