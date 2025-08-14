from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.CharField(default=True, max_length=1)
    paid_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)