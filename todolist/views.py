from django.shortcuts import render
from .models import Todo
from .forms import TodoForm
from django.utils import timezone
from django.shortcuts import redirect
# from django.http import HttpResponse

def todo(request):
    todos = Todo.objects.all()
    return render(request, 'todolist/todo_list.html', {'listitem': todos})

def new_todo(request):
    if request.method == "POST":
        if form.is_valid():
            text= request.POST['text']
            # new_todo.created_date = timezone.now()
            new_todo = Todo(text=text) 
            new_todo.save()
    else:
        form = TodoForm()
        return render(request, 'todolist/todo_list.html', {'form': form})

'''
if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            new_todo = form.save(commit=False)
            new_todo.created_date = timezone.now()
            new_todo.save()
            return redirect('todo')
'''
