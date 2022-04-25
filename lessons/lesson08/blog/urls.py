from django.urls import path

from .views import index, post, create

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:pk>', post, name='post'),
    path('create/', create, name='create'),
]
