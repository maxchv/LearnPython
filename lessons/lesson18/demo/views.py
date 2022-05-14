from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from demo.models import Task
from demo.serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
