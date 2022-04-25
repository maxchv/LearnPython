from django.urls import path

from .views import index, post, student, details

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:pk>', post, name='post'),
    path('students/', student, name='student'),
    path('details/<int:pk>', details, name='details'),

]
