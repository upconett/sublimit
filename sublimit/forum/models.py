from django.db import models

from user.models import User


class Article(models.Model):
    author = models.ForeignKey("user.User", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=10000)
