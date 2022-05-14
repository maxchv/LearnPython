from django.urls import path
from django.views.generic import TemplateView

from demo.views import EmailView

app_name = 'demo'

urlpatterns = [
    path('', TemplateView.as_view(template_name='demo/index.html'), name='index'),
    path('email/', EmailView.as_view(), name='email'),
]
