from django.shortcuts import render , redirect
from django.http import HttpResponse, response
from .form import *
from .models import *
from django.core import serializers


def home_app(request):
    return render(request, "todo/meta/home.html",{})


def create_list(request):
    if request.method == "POST":
        list_forms = ListCreation(request.POST or None)
        if list_forms.is_valid():
            list_forms.save()
            return redirect('/List')
    else:
        list_forms = ListCreation()        
    return render(request,'todo/base/createList.html',{"form":list_forms})

def improvementpage(response):
    return render(response, 'todo/base/improvements.html',{})

def view_lists(request):
    if request.method == "POST":
        todoList =  TodoApp_Fields.objects.all()
        if request.POST.get(todoList.activity):
            TodoApp_Fields.objects.filter(todoList.activity).delete()
    else:
        todoList =  TodoApp_Fields.objects.all()

    return render(request,'todo/base/lists.html',{"todolist":todoList})

def deleteTask(request, todo_id):

    TodoApp_Fields.objects.get(id=todo_id).delete()
    return redirect('/List')

def aboutpage(request):
    return render(request, 'todo/base/aboutme.html', {})
    

def deleteall(request):
    TodoApp_Fields.objects.all().delete()
    return redirect('/List')



