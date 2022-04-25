from django.urls import path

from .views import index, save

urlpatterns = [
    path('', index),
    path('save', save, name='save')
]