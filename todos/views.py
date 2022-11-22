from django.shortcuts import render
from rest_framework import generics

from todos.models import Todo
from todos.serializers import TodoSerializer


class TodoList(generics.ListAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    class Meta:
        model = Todo
