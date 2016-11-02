from django.conf.urls import url
from .views import bookmark_list, bookmark_user, \
                   bookmark_create, bookmark_edit

urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', bookmark_user, name='marcador_bookmark_user'),
    url(r'^$', bookmark_list, name='marcador_bookmark_list'),
    url(r'^create/$', bookmark_create, name="marcador_bookmark_create"),
    url(r'^edit/(?P<pk>\d+)/$', bookmark_edit, name="marcador_bookmark_edit"),
]