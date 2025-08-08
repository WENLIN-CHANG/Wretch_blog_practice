from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Article
from django.contrib import messages
from .forms import ArticleForm
from comments.forms import CommentForm
from django.views.decorators.http import require_POST

def index(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        form.save()

        messages.success(request, "新增成功")
        return redirect("articles:index")
    else:
        articles = Article.objects.order_by("-id")
        return render(request, "articles/index.html", {"articles": articles})

def create(request):
    form = ArticleForm()
    return render(request, "articles/create.html", {"form": form})

def detail(request, id):
    article = get_object_or_404(Article, pk=id)

    if request.POST:
        if request.POST["_method"] == "patch":
            form = ArticleForm(request.POST, instance=article)
            form.save()

            messages.success(request, "更新成功")
            return redirect("articles:detail", article.id)

        if request.POST["_method"] == "delete":
            article.delete()

            messages.warning(request, "刪除成功")
            return redirect("articles:index")
    else:
        comment_form = CommentForm()
        comments = article.comment_set.filter(deleted_at = None).order_by("-id")
        return render(
            request,
            "articles/detail.html",
            {
                "article": article, 
                "comment_form": comment_form, 
                "comments": comments
            },
        )


def edit(request, id):
    article = get_object_or_404(Article, pk=id)
    form = ArticleForm(instance=article)
    return render(request, "articles/edit.html", {"article": article, "form": form})
