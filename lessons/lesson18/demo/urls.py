from django.urls import path, include
from rest_framework import routers

from demo.views import TaskViewSet

app_name = 'demo'

router = routers.DefaultRouter()
router.register('todos', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
