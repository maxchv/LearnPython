from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def welcome(request):
    return HttpResponse("<h1>Hello Django!!!</h1>")

def index(request):
    return HttpResponse("<h1>Index Page</h1>")
