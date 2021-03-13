from account.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout, login
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def accountView(request,usr=User.Username):

    if request.method == "GET":
        accInfo = AccountsDB.objects.filter(Username=usr)
    else:
        accInfo = AccountsDB.objects.get(Username=usr)

    return render(request,'todo/UserCreation/account_view.html',{'accinfo':accInfo})

def register_(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}')
            form.save()
            return redirect('/login')
    else:
        form = UserCreationForm()
    return render(request, 'todo/UserCreation/register.html', {'form':form})


# def register_(request):
#     if request.method == "POST":
#         reg_ = Register(request.POST or None)
#         if reg_.is_valid():
#             reg_.save()
#             if reg_.save() == True or not None:
#                 return redirect('/login')
#     else:
#         reg_ = Register()
#     return render(request, 'todo/UserCreation/register.html', {'form':reg_})
    
def dashboard(request):
    return render(request, "todo/tut_temps/dashboard.html")


def logout_(request):
    # username = request.session.get(f'loggedin', '{username}')
    logout(request)
    
    return redirect('/')

