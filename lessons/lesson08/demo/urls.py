from django.urls import path

from .views import index, create, details, delete, edit

app_name = 'demo'

urlpatterns = [
    path("", index, name='index'),
    path("create/", create, name='create'),
    path("details/<int:pk>/", details, name='details'),
    path("edit/<int:pk>/", edit, name='edit'),
    path("delete/<int:pk>/", delete, name='delete'),
]
