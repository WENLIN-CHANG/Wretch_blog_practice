from django.shortcuts import render, redirect
from .models import Article

def index(request):
    if request.POST:
        title = request.POST['title']
        content = request.POST["content"]
        # 寫入 table
        Article.objects.create(title=title, content=content)
        return redirect("pages:home")
    else:
        return render(request, "articles/index.html")

def create(request):
    return render(request, "articles/create.html")
