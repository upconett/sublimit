from django.db import models


class User(models.Model):
    email: models.EmailField = models.EmailField()
    username: models.CharField = models.CharField(max_length=20, unique=True)
    password: models.CharField = models.CharField(max_length=35)
    avatar: models.ImageField = models.ImageField(null=True)

    def __str__(self):
        return self.username


class Contact(models.Model):
    TELEGRAM = 'TG'
    GITHUB = 'GH'
    CONTACT_TYPE_CHOICES = {
        TELEGRAM: "Telegram",
        GITHUB: "GitHub"
    }

    user = models.ForeignKey("User", on_delete=models.CASCADE)
    type = models.CharField(
        max_length=2,
        choices=CONTACT_TYPE_CHOICES
    )
    link = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.type}, {self.link}'


class Article(models.Model):
    author = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=10000)
