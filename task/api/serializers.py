from rest_framework.serializers import ModelSerializer

from task.models import Task


class TaskModelSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
