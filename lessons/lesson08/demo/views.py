from django.shortcuts import render, redirect, get_object_or_404

from .forms import StudentForm
from .models import Student


def index(request):
    queryset = Student.objects.all()
    context = {'students': queryset}
    template_name = 'demo/index.html'
    return render(request, template_name, context)


def create(request):
    if request.method == 'GET':
        form = StudentForm()
    elif request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("demo:index")
    context = {
        'form': form,
        'title': 'Create student'
    }
    template_name = "demo/create.html"
    return render(request, template_name, context)


def edit(request, pk):
    # try:
    #     student = Student.objects.get(pk=pk)
    # except:
    #     return HttpResponse("404 Not found", status=404)
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        form = StudentForm(instance=student)
    elif request.method == 'POST':
        form = StudentForm(instance=student, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('demo:edit', pk)
    template_name = 'demo/create.html'
    context = {'form': form, 'title': 'Edit student'}
    return render(request, template_name, context)


def details(request, pk):
    queryset = get_object_or_404(Student, pk=pk)  # Student.objects.get(pk=pk)
    context = {'student': queryset}
    return render(request, 'demo/details.html', context)


def delete(request, pk):
    student = get_object_or_404(Student, pk=pk) # Student.objects.get(pk=pk)
    student.delete()
    return redirect("demo:index")
