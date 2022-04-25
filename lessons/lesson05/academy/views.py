from django.shortcuts import render, redirect
from datetime import date

from .models import Student


def index(request):
    return render(request, 'index.html', {
        'students': Student.objects.all()
    })


def save(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    elif request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        bdate = request.POST.get('bdate')
        print(f'Save {fname} {lname} {bdate}')
        Student.objects.create(first_name=fname, last_name=lname, birth_date=date.fromisoformat(bdate))
        return redirect("/")
