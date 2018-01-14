from django.shortcuts import render

def todo(request):
    return render(request, 'todolist/todo_list.html')