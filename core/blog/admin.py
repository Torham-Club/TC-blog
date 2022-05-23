from django.contrib import admin
from blog.models import  UsersAdditionalInfo, Posts, FollowersAndFollowing, Comment
# Register your models here.

admin.site.register(FollowersAndFollowing)
admin.site.register(UsersAdditionalInfo)
admin.site.register(Posts)
admin.site.register(Comment)