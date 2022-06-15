from django.db.models import Q
from django.shortcuts import render

from .forms import PostForm
from .models import Post


def index(request):
    q = request.GET.get('q')
    if q:
        posts = Post.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
    else:
        posts = Post.objects.all()
    return render(request, 'blog/index.html',
                  context={'posts': posts, 'q': q})


def post(request, pk):
    return render(request, 'blog/post.html')


def create(request):
    context = {
        "form": PostForm()
    }
    return render(request, "blog/create_post.html", context)
