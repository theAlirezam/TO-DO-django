from django.urls import path
from main.views import index, add_todo, complete_todo, delete_completed, delete_all

urlpatterns = [
    path('', index, name='index'),
    path('add', add_todo, name='add'),
    path('complete<int:todo_id>', complete_todo, name='complete'),
    path('deletecomplited', delete_completed, name='delete_completed'),
    path('deletealll', delete_all, name='delete_all'),

]
