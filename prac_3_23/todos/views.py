from django.shortcuts import render, redirect
from .forms import TodoForms
from .models import Todo
# Create your views here.

def index(request):
    print('index 함수 도착')
    form = TodoForms()
    todo_list = Todo.objects.all() # 모든 Todo data 조회
    context = {
        'form' : form,
        'todo_list' : todo_list
    }
    return render(request, 'todos/index.html', context)


def create(request):
    print('create 함수 도착')
    if request.method == 'POST': # Todo 작성 요청
        print(request.POST)
        form = TodoForms(request.POST)
        print('POST')
        if form.is_valid(): # 유효성 검사 -> cleaned_data(dict) => clean_field
            form.save()
        return redirect('index')
        
    else:
        form = TodoForms()
    context = {
        'form' : form,
    }
    return render(request, 'todos/index.html', context)


def update(request, pk):
    todo = Todo.objects.get(pk = pk)
    print('update')
    if request.method == 'POST':
        form = TodoForms(request.POST, instance=todo)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = TodoForms(instance=todo)
    context = {
        'form' : form,
        'todo' : todo,
    }    
    return render(request, 'todos/update.html', context)
    
def delete(request, pk):
    if request.method == "POST":
        todo = Todo.objects.get(pk = pk)
        todo.delete()
        return redirect('index')
    
def done(request, pk):
    todo = Todo.objects.get(pk = pk)
    todo.isCompleted = True
    todo.save()
    
    return redirect('index')