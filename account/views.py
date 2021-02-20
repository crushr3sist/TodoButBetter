from account.models import AccountsDB
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def accountView(request,usr=AccountsDB.Username):

    if request.method == "POST":
        accInfo = AccountsDB.objects.get(Username=usr)
    else:
        accInfo = AccountsDB.objects.get(Username=usr)

    return render(request,'todo/UserCreation/account_view.html',{'accinfo':accInfo})