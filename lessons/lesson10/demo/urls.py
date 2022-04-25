from django.urls import path

from demo.views import StudentList, CreateStudentView

app_name = 'demo'

urlpatterns = [
    path('', StudentList.as_view(), name='index'),
    path('create/', CreateStudentView.as_view(), name='create'),
]
