from django.contrib import admin

# Register your models here.
from django.contrib import admin
from todo.models import TodoModel

admin.site.register(TodoModel)
