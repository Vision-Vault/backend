from .models import Post
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer
from django.views.generic import ListView,DetailView
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpRequest, HttpResponse


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        status = self.kwargs.get('status')
        return Post.objects.filter(status=status)
