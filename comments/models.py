from django.db import models
from django.contrib.auth import get_user_model
from posts.models import Post
from django.urls import reverse_lazy, reverse

# Create your models here.

class Shared(models.Model):
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    class Meta:
        abstract=True

class Comment(Shared):
    project=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')

    def __str__(self) -> str:
        return self.user

class ChildComment(Shared):
    parent_comment=models.ForeignKey(Comment,on_delete=models.CASCADE,related_name='Child_Comments')

    def __str__(self) -> str:
        return self.user

