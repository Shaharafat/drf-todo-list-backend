from django.contrib import admin

from .models import Tag, Todo

# Register your models here.
admin.site.register(Todo)
admin.site.register(Tag)
