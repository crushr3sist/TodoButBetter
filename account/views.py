from account.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout, login
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def accountView(request,usr=User.Username):

    if request.method == "GET":
        accInfo = User.objects.filter(Username=usr)
    else:
        accInfo = User.objects.get(Username=usr)

    return render(request,'todo/UserCreation/account_view.html',{'accinfo':accInfo})

def register_(request):
    if request.method == "POST":
        form = reg_user(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}')
            form.save()
            return redirect('/login')
    else:
        form = reg_user()
    return render(request, 'todo/UserCreation/register.html', {'form':form})
    
def dashboard(request):
    return render(request, "todo/tut_temps/dashboard.html")


def logout_(request):
    logout(request)    
    return redirect('/')

