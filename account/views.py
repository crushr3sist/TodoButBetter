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
            return redirect('/user/login_/')
    else:
        reg_ = Register()
    return render(request, 'todo/UserCreation/register.html', {'form':reg_})
    
def login_(request,usr=AccountsDB.Username):
    # clean the data from the form and use that as the usr
    if request.method == "POST":
        login = Login(request.POST or None)
        if login.is_valid():
            username = login.cleaned_data['Username']
            password = login.cleaned_data['Password']
            remember_me = login.cleaned_data['remember_me']
            user = authenticated(username=username, password=password)
    else:
        login = Login()
    return render(request, 'todo/UserCreation/login.html', {'login':login})
    

