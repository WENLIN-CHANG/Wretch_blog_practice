from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Article
from django.contrib import messages

def index(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get("content")
        is_published = request.POST.get("is_published")
        # 寫入 table
        Article.objects.create(title=title, content=con
                               tent, is_published=is_published)
        messages.success(request, "新增成功")
        return redirect("articles:index")
    else:
        articles = Article.objects.order_by("-id")
        return render(request, "articles/index.html", {"articles": articles})

def create(request):
    return render(request, "articles/create.html")

def detail(request, id):
    article = get_object_or_404(Article, pk=id)

    if request.POST:
        if request.POST["_method"] == "patch":
            article.title = request.POST.get("title")
            article.content = request.POST.get("content")
            article.is_published = request.POST.get("is_published") == "on"
            article.save()

            messages.success(request, "更新成功")
            return redirect("articles:detail", article.id)

        if request.POST["_method"] == "delete":
            article.delete()

            messages.warning(request, "刪除成功")
            return redirect("articles:index")
    else:
        return render(request, "articles/detail.html", {"article": article})


def edit(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, "articles/edit.html", {"article": article})
