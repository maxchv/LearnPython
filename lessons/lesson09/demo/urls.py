from django.urls import path

from .views import StudentView, StudentDetailsView

urlpatterns = [
    path('', StudentView.as_view(), name='index'),
    path('student/<int:pk>', StudentDetailsView.as_view(), name='details')
    # path('groups/', StudentGroupView.as_view(), name='groups'),
]
