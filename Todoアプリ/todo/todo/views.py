from django.shortcuts import render
from django.views import generic
from .models import TodoModel
from django.urls import reverse_lazy

# Create your views here.
class TodoList(generic.ListView):
    #template_name = 'todo/list.html'
    template_name = 'todo/todo_list.html'
    model = TodoModel
    context_object_name = 'todos'


class TodoDetail(generic.DetailView):
    #template_name = 'todo/detail.html'
    template_name = 'todo/todo_detail.html'
    model = TodoModel


class TodoUpdate(generic.UpdateView):
    #template_name = 'todo/update.html'
    template_name = 'todo/todo_update.html'
    model = TodoModel
    fields = ('title', 'content', 'deadline')
    #success_url = reverse_lazy('list')
    success_url = reverse_lazy('todo_list')


class TodoDelete(generic.DeleteView):
    #template_name = 'todo/delete.html'
    template_name = 'todo/todo_delete.html'
    model = TodoModel

    #success_url = reverse_lazy('list')
    success_url = reverse_lazy('todo_list')


class TodoCreate(generic.CreateView):
    #template_name = 'todo/create.html'
    template_name = 'todo/todo_create.html'
    model = TodoModel
    fields = ('title', 'content', 'deadline')

    success_url = reverse_lazy('todo_list')

    #success_url = reverse_lazy('list')