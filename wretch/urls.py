from django.contrib import admin
from django.urls import path
from django.shortcuts import render


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('about/', about),
    path('', home),
]
