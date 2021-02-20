from account.models import AccountsDB
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import *

# Create your views here.
def accountView(request,usr=AccountsDB.Username):

    if request.method == "GET":
        accInfo = AccountsDB.objects.filter(Username=usr)
    else:
        accInfo = AccountsDB.objects.get(Username=usr)

    return render(request,'todo/UserCreation/account_view.html',{'accinfo':accInfo})

def register_(request):
    if request.method == "POST":
        reg_ = Register(request.POST or None)
        if reg_.is_valid():
            reg_.save()
    else:
        reg_ = Register()
    return render(request, 'todo/UserCreation/register.html', {'form':reg_})
    
def login_(request):
    if request.method == "POST":
        reg__ = Login(request.POST or None)
        if reg__.is_valid():
            reg__.save()
            return redirect('register__/')
    else:
        reg__ = Login()
    return render(request, 'todo/UserCreation/login.html', {'form':reg__})
    

