from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelField):
    class Meta:
       model = 'Task'
       fields = ('id', 'title', 'description', 'done')

    