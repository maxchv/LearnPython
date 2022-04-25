from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from demo.models import Student


# class StudentList(TemplateView):
#     template_name = 'demo/index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         page = int(self.request.GET.get('page', 1))
#         per_page = int(self.request.GET.get('per_page', 10))
#         # context['students'] = Student.objects.all()[(page-1)*per_page:(page*per_page)]
#         paginator = Paginator(Student.objects.all(), per_page)
#         context['page_obj'] = paginator.page(page)
#         start = page - 1 if page - 1 > 0 else 1
#         context['page_range'] = paginator.page_range[start:page+5]
#         return context

class StudentList(ListView):
    model = Student
    # template_name_suffix = 's'
    # ordering = 'birth_date'
    context_object_name = 'students'
    # queryset = Student.objects.all()[:10]
    template_name = 'demo/index.html'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        queryset = self.get_queryset()
        paginator = self.get_paginator(queryset, self.get_paginate_by(queryset))
        page = int(self.request.GET.get('page', 1))
        start = page - 1 if page - 1 > 0 else 1
        context['page_range'] = paginator.page_range[start:page + 5]
        return context


class CreateStudentView(CreateView):
    model = Student
    fields = ('first_name', 'last_name', 'gender', 'birth_date')


class UpdateStudentView(UpdateView):
    model = Student


class DeleteStudentView(DeleteView):
    model = Student
