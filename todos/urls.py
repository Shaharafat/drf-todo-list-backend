from django.urls import path

from todos import views

urlpatterns = [
    path("", views.TodoList.as_view()),
    path("create-todo/", views.CreateTodo.as_view()),
]
