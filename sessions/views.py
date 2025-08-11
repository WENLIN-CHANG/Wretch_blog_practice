from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login
from django.contrib import messages

def new(request):
    return render(request, "sessions/new.html")

@require_POST
def create(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
        
    if user:
        login(request, user)
        messages.success(request, "登入成功")
        return redirect("articles:index")
    else:
        messages.error(request, "登入失敗")
        return redirect("sessions:new")

