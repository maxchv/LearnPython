from django.urls import path

from .views import create, StudentListView, CreateStudentView

app_name = 'demo'

urlpatterns = [
    path('', StudentListView.as_view(), name='index'),
    path('create/', CreateStudentView.as_view(), name='create'),
]
