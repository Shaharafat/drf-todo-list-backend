from django.shortcuts import render
from rest_framework import generics

from todos.models import Todo
from todos.serializers import TodoCreateSerializer, TodoSerializer


class TodoList(generics.ListAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    class Meta:
        model = Todo


class CreateTodo(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoCreateSerializer

    class Meta:
        model = Todo


class UpdateTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = "pk"
