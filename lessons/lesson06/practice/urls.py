from django.urls import path

from practice.views import task01

urlpatterns = [
    path('task01/', task01),
]