from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from demo.forms import StudentForm
from demo.models import Student


def create(request):
    context = {'form': StudentForm}
    if request.method == 'POST':
        print('FILES: ', request.FILES)
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            redirect('demo:index')
        else:
            context['form'] = form
    return render(request, 'demo/create.html', context)


class CreateStudentView(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'demo/create.html'
    success_url = reverse_lazy('demo:index')


class StudentListView(ListView):
    model = Student
    template_name = 'demo/index.html'
    paginate_by = 10
    context_object_name = 'students'
