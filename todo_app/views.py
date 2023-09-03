from django.shortcuts import render,HttpResponse
from rest_framework import viewsets, permissions
from .models import todo
from .serializers import *


class TodoListView(viewsets.ModelViewSet):
    queryset = todo.objects.filter(is_complete=False)
    serializer_class = GetTodolist

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]