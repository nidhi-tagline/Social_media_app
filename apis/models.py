from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class Profile(BaseModel):
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.CharField(max_length=200, blank=True, null=True)
    profile_pic = models.ImageField(upload_to="profile_pics/", default="default.png")
    DOB = models.DateField(blank=True, null=True)

    # return the number of friends
    def friend_count(self):
        user = Friend.objects.get(user=self.username)
        return user.friend.count()

    def __str__(self):
        return f"{self.username}'s Profile"


class Post(BaseModel):
    description = models.CharField(max_length=200, blank=True, null=True)
    media = models.FileField(upload_to="post_uploads/")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    liked_by = models.ManyToManyField(User, related_name="likes")

    # return the number of likes
    def likes_count(self):
        return self.liked_by.count()

    def __str__(self):
        return f"{self.description}-{self.created_by}"


class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=200, blank=True, null=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment"
    )
    reply = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, related_name="replies"
    )

    def __str__(self):
        if len(self.comment) > settings.TRUNCATE_CHAR_LIMIT:
            return f"{self.comment[:settings.TRUNCATE_CHAR_LIMIT]}...-{self.created_by}"
        else:
            return f"{self.comment} -{self.created_by}"


class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friends")
    friend = models.ManyToManyField(User, blank=True, related_name="friend")

    # add user to friend list
    def add_friend(self, user):
        if not user in self.friend.all():
            self.friend.add(user)
            self.save()

    # remove user from friend list
    def remove_friend(self, user):
        if user in self.friend.all():
            self.friend.remove(user)
            self.save()

    def __str__(self):
        return f"{self.user}({self.friend.count()})"


class FriendRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="receiver"
    )
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender}->{self.receiver}"
