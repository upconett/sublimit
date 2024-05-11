from django.db import models

from user.models import User


class Article(models.Model):

    AMAZON = 'AM'
    UIUX = 'UI'
    PHYSICS = 'PH'
    FRONTEND = "FR"
    BACKEND = "BA"
    TAG_CHOICES = {
        AMAZON: "amazon",
        UIUX: "uiux",
        PHYSICS: "physics",
        FRONTEND: "frontend",
        BACKEND: "backend"
    }

    author = models.ForeignKey("user.User", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=10000)
    tag = models.CharField(
        max_length=2,
        choices=TAG_CHOICES,
        null=True
    )
