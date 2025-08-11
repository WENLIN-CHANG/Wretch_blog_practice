from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib import messages

def new(request):
    return render(request, "users/new.html")

@require_POST
def create(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    if username != '' and password != '':
        user = User.objects.create_user(
            username=username, 
            password=password
        )

        if user:
            messages.success(request, "註冊成功")
            return redirect("articles:index")
        else:
            messages.error(request, "註冊失敗")
            return redirect("users:new")
        
    else:
      return redirect("users:new")
