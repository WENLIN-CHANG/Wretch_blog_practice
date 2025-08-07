from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Article

def index(request):
    if request.POST:
        title = request.POST['title']
        content = request.POST["content"]
        # 寫入 table
        Article.objects.create(title=title, content=content)
        return redirect("articles:index")
    else:
        articles = Article.objects.all().order_by("-id")
        return render(request, "articles/index.html", {"articles": articles})

def create(request):
    return render(request, "articles/create.html")

def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, "articles/detail.html", {"article": article})
