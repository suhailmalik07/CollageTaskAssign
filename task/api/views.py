from rest_framework.viewsets import ModelViewSet

from .serializers import TaskModelSerializer
from task.models import Task


class TaskModelViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
