from django.db import models
from django.contrib.auth.models import User


class UsersAdditionalInfo(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="info"
    )

    bio = models.CharField(max_length=500, null=True, blank=True)
    profile_picture = models.ImageField()

    def __str__(self) -> str:
        return self.user.username


class Posts(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    title = models.CharField(max_length=300)
    slug = models.SlugField(null=True)
    content = models.TextField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
