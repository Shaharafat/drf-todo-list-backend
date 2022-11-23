from rest_framework import serializers

from todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    tag_name = serializers.CharField(source="tags.title", read_only=True)

    class Meta:
        model = Todo
        fields = ["id", "title", "completed", "tag_name", "createdAt", "updatedAt"]


class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["title", "completed", "tags", "createdAt", "updatedAt"]
