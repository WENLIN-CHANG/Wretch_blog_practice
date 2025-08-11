from django.shortcuts import redirect, get_object_or_404,render
from .forms import CommentForm
from articles.models import Article
from django.contrib import messages
from comments.models import Comment
from django.views.decorators.http import require_http_methods, require_POST
from django.http import HttpResponse

def create(request, id):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=id)

        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.article = article
        comment.save()

        # messages.success(request, "新增留言成功")
        return render(request, "comments/comment.html", {"comment": comment})
        # return redirect("articles:detail", article.id)

@require_http_methods(["DELETE"])
def delete(request, id):
    comment = get_object_or_404(Comment, pk=id)
    comment.delete()
    # messages.warning(request, "刪除留言成功")

    return HttpResponse("")
    # return redirect("articles:detail", comment.article_id)
