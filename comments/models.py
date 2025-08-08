from django.db import models
from articles.models import Article


class Comment(models.Model):
    content = models.TextField(null=False)
    article = models.ForeignKey(Article, default=None, on_delete=models.CASCADE)
    # 建立時間
    created_at = models.DateTimeField(auto_now_add=True)
    # soft delete, 加索引 index
    deleted_at = models.DateTimeField(null=True, db_index=True)
