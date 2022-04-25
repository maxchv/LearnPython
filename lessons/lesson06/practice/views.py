from django.shortcuts import render

from .models import Person


# Create your views here.
def task01(request):
    return render(request, 'task01.html', {
        'man': Person.objects.all().filter(age__range=(18, 61), gender='MALE')
    })

