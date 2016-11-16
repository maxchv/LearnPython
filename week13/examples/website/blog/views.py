from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag


def get_categories():
    categories = Category.objects.all()
    half = categories.count() / 2 + 1
    return {"categories1": categories[:half], "categories2": categories[half:]}


def index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    context.update(get_categories())
    return render(request, "blog/index.html", context)


def post(request, pk):
    categories = Category.objects.all()
    if not pk:
        pk = 1
    post = get_object_or_404(Post, pk=pk)
    context = {"post": post}
    context.update(get_categories())
    return render(request, "blog/post.html", context)


def category(request, pk):
    posts = Post.objects.filter(category__pk=pk)
    context = {"posts": posts}
    context.update(get_categories())
    return render(request, "blog/index.html", context)


def search(request):
    posts = Post.objects.filter(content__icontains=request.POST['keywords'])
    context = {"posts": posts}
    context.update(get_categories())
    return render(request, "blog/index.html", context)