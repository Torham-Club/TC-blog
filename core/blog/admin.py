from django.contrib import admin
from blog.models import  UsersAdditionalInfo, Posts, FollowersAndFollowing
# Register your models here.

admin.site.register(FollowersAndFollowing)
admin.site.register(UsersAdditionalInfo)
admin.site.register(Posts)