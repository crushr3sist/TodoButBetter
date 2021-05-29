from django.shortcuts import render , redirect
from django.http import HttpResponse, response
from .form import *
from .models import *
from django.core import serializers
from django.contrib.auth.decorators import login_required


def home_app(request):
    if request.user.is_authenticated:
        return redirect('/List')
    return render(request, "todo/meta/home.html",{})

@login_required(login_url='/login/')
def profile_page(request):
    return render(request, 'todo/Profile/base.html')

@login_required(login_url='/login/')
def create_list(request):
    if request.method == "POST":
        list_forms = ListCreation(request.POST or None)
        if list_forms.is_valid():
            check_auth = request.user.is_authenticated
            if check_auth is True:
                post = list_forms.save(commit=False)
                post.author_id = request.user.id
                post.save()
                return redirect('/List')
    else:
        list_forms = ListCreation()        
    return render(request,'todo/base/createList.html',{"form":list_forms})

@login_required(login_url='/login/')
def improvementpage(response):
    return render(response, 'todo/base/improvements.html',{})

@login_required(login_url='/login/')
def view_lists(request):
    if request.method == "POST":
        todoList = TodoApp_Fields.objects.filter(author_id=request.user.id)
        username = request.user.username
        if request.POST.get(todoList.activity):
            TodoApp_Fields.objects.filter(todoList.activity).delete()
    else:
        todoList = TodoApp_Fields.objects.filter(author_id=request.user.id)
        username = request.user.username
    return render(request,'todo/base/lists.html',{"todolist":todoList,"username":username})

@login_required(login_url='/login/')
def deleteTask(request, todo_id):

    TodoApp_Fields.objects.get(id=todo_id).delete()
    return redirect('/List')


@login_required(login_url='/login/')
def edit_element(request, todo_id):
    if request.method == "POST":
        list_forms = ListCreation(request.POST or None)
        if list_forms.is_valid():
            check_auth = request.user.is_authenticated
            if check_auth is True:
                post = list_forms.save(commit=False)
                post.author_id = request.user.id
                post.save()
                return redirect(f'/deleteTask/{todo_id}')
    else:
        todoList = TodoApp_Fields.objects.filter(id=todo_id)
        for k in todoList:

            list_forms = ListCreation(initial={
                'activity':k.activity,
                'urgency':k.urgency,
                'DueDate':k.DueDate,
                })        
    return render(request,'todo/base/edit.html',{"form":list_forms, })
    
@login_required(login_url='/login_/')
def aboutpage(request):
    return render(request, 'todo/base/aboutme.html', {})
    
@login_required(login_url='/login/')
def deleteall(request):
    TodoApp_Fields.objects.all().delete()
    return redirect('/List')



