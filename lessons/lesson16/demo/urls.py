from django.urls import path
from .views import TasksListView, TasksDeleteView

app_name = 'demo'

urlpatterns = [
    path('', TasksListView.as_view(), name='index'),
    path('delete/<int:pk>', TasksDeleteView.as_view(), name='delete'),
]