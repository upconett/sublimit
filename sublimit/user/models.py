from django.db import models


class User(models.Model):
    username: models.CharField = models.CharField(max_length=20, unique=True)
    email: models.EmailField = models.EmailField()
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



class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['follower', 'followed'], name='unique_followship'),
        ]

    def __str__(self):
        return f'{self.follower} follows {self.followed}'