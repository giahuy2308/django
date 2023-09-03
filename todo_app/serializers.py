from rest_framework import serializers
from .models import *


class GetTodolist(serializers.ModelSerializer):

    class Meta:
        model = todo
        fields = '__all__'


# class PostTodo(serializers.Serializer):
#     title = serializers.CharField(max_length=100,default='')
#     description = serializers.TextField(max_length=1000,default='')
#     avatar = serializers.ImageField(upload_to="static/image")
#     source = serializers.CharField(max_length=100,default='')
#     is_complete = serializers.BooleanField(default=False)