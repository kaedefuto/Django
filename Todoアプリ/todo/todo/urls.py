from django.urls import path
#from .views import TodoList, TodoDetail
#from .views import TodoList, TodoDetail, TodoUpdate, TodoDelete, TodoCreate
from . import views
app_name = 'todo'
"""
urlpatterns = [
    path('list/', TodoList.as_view(), name='list'),
    path('detail/<int:pk>/', TodoDetail.as_view(), name='detail'),
    path('update/<int:pk>/', TodoUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', TodoDelete.as_view(), name='delete'),
    path('create/', TodoCreate.as_view(), name='create'),
]
"""
urlpatterns = [
    path('', views.TodoList.as_view(), name='todo_list'),
    path('todo_detail/<int:pk>/',
         views.TodoDetail.as_view(),
         name='todo_detail'),
    path('todo_update/<int:pk>/',
         views.TodoUpdate.as_view(),
         name='todo_update'),
    path('todo_delete/<int:pk>/',
         views.TodoDelete.as_view(),
         name='todo_delete'),
    path('todo_create/', views.TodoCreate.as_view(), name='todo_create'),
]