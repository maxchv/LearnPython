from django.shortcuts import render
import random
from django.utils import timezone


def dummy():
    return str(random.randint(100, 1000))

# Create your views here.
def index(request):
    title = "My Blog"
    lst = ["one", "two", "three"]
    return render(request, "blog/index.html", {"title": title,
                                               "var": dummy,
                                               "date": timezone.now(),
                                               "list_data": lst})

def form(request):
    return render(request, "blog/form.html")

def save(request):
    title = request.POST.get('title', '')
    content = request.POST.get('content', '')
    return  render(request, "blog/save.html", {"title": title, "content": content})