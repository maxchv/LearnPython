from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView

from .forms import TaskForm
from .models import Task


class TasksListView(ListView):
    model = Task
    template_name = 'demo/index.html'
    context_object_name = 'tasks'
    extra_context = {'form': TaskForm(), 'title': 'Demo'}
    paginate_by = 10

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
        return redirect("demo:index")


class TasksDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('demo:index')

#
# def task_list(request):
#     tasks = Task.objects.all()
#     data = []
#     for task in tasks:
#         data.append({
#             "description": task.description,
#             "created": str(task.created)
#         })
#     return JsonResponse(data, safe=False)
