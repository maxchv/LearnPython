from django.urls import path
from django.views.generic import TemplateView

from demo.views import login_view, create_post, logout_view, OnlyForAuthenticatedUsersView, delete_post

app_name = 'demo'

urlpatterns = [
    path('', TemplateView.as_view(template_name='demo/index.html'), name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('post/', create_post, name='create_post'),
    path('delete/', delete_post, name='delete_post'),
    path('secured/', OnlyForAuthenticatedUsersView.as_view())
]