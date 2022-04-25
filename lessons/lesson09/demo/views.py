from django.shortcuts import redirect
from django.views.generic import TemplateView

# class TemplateMixin:
#     template_name = 'demo/index.html'
#
#     def get_template_name(self):
#         return self.template_name
#
#
# class FormMixin:
#     cls = None
#
#     def get_form_class(self):
#         return self.cls
#
#     def get_template_name(self):
#         return None
#
#     def get(self, request):
#         cls = self.get_form_class()
#         form = cls()  # form = StudentForm()
#         context = {'form': form}
#         return render(request, self.get_template_name(), context)
#
#     def post(self, request):
#         cls = self.get_form_class()
#         form = cls(data=request.POST)
#         form.save()
#         return redirect("/")


# class StudentView(TemplateMixin, FormMixin, View):
#     template_name = 'demo/index.html'
#     cls = StudentForm
#
#
# class StudentGroupView(TemplateMixin, FormMixin, View):
#     template_name = 'demo/index.html'
#     cls = StudentGroupForm
from demo.forms import StudentForm
from demo.models import Student


class StudentView(TemplateView):
    template_name = 'demo/index.html'
    extra_context = {'title': 'Student form'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StudentForm()
        return context

    def post(self, request):
        form = StudentForm(data=request.POST)
        form.save()
        return redirect("index")


class StudentDetailsView(TemplateView):
    template_name = 'demo/student_details.html'

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        context = super(StudentDetailsView, self).get_context_data()
        context['student'] = Student.objects.get(pk=pk)
        return context
