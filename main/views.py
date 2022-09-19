from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from main.form import TodoForm
from main.models import Todo


# Create your views here.
def index(request):
    todo_list = Todo.objects.order_by('id')
    form = TodoForm()
    context = {'todo_list': todo_list, 'form': form}
    return render(request, 'todo/index.html', context)


@require_POST
def add_todo(request):
    form = TodoForm(request.POST)
    print(request.POST['text'])

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()
    return redirect('index')


def complete_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')


def delete_completed(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')


def delete_all(request):
    Todo.objects.all().delete()
    return redirect('index')
