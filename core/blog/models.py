from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.contrib.auth import get_user_model


class FollowersAndFollowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    follwers = models.ManyToManyField(
        get_user_model(),
        blank=True,
        related_name='follwers'
    )
    following = models.ManyToManyField(
        get_user_model(),
        blank=True,
        related_name='following'
    )


class UsersAdditionalInfo(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='info'
    )

    bio = models.CharField(max_length=500, null=True, blank=True)
    profile_picture = models.ImageField()

    def __str__(self) -> str:
        return self.user.username


class Posts(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    title = models.CharField(max_length=300)
    slug = models.SlugField(null=True)
    content = models.TextField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Posts, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.author.username} | {self.title}"
