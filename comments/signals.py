from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Comment

@receiver(post_save, sender=Comment)
def created_or_delete(sender, instance, created, **kwargs):
    username = instance.user.username

    if created:
        print(f"{username} 新增留言")
    else:
        print(f"{username} 刪除留言") 

