from .models import Post
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer
from django.views.generic import ListView,DetailView
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpRequest, HttpResponse


class PostListView(ListView):
    # model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(status = Post.ACTIVE)
