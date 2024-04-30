from django.contrib import admin

from .models import Comment, Friend, FriendRequest, Post, Profile, User

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Friend)
admin.site.register(FriendRequest)
