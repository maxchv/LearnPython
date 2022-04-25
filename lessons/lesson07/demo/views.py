from django.shortcuts import render

from datetime import date

from .forms import StudentForm
from .models import Student


def index(request):
    return render(request, 'index.html')


def post(request, pk=None):
    print(f'pk = {pk} {type(pk)}')
    return render(request, 'post.html', {'pk': pk})


def student(request):
    form = StudentForm({'first_name': 'Вася'})
    if request.method == 'GET':
        print(form)
        print(form.as_p())
        print(form.as_ul())
    elif request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        Student.objects.create(first_name=first_name, last_name=last_name,
                               date_of_birth=date.fromisoformat(date_of_birth))
    return render(request, 'student.html', {
        'form': form, 'students': Student.objects.all()
    })


def details(request, pk=None):
    return render(request, 'details.html', {
        'student': Student.objects.get(pk=pk)
    })
