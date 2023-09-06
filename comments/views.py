from .models import Comment,ChildComment
from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .form import CommentForm,CommentForm2
from posts.models import Post
from accounts.models import CustomUser
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from posts.permissions import IsOwnerOrReadOnly
# Create your views here.
class PostDetailView(DetailView):

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        context={}
        slugs=kwargs.get('slug',"no slug")
        post=get_object_or_404(Post,slug=slugs)
        context['post']=post
        form=CommentForm()
        context['form']=form

        return render(request,'comments/post_detail.html',context)


    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        slugs=kwargs.get('slug',"no slug")
        post=get_object_or_404(Post,slug=slugs)
        user=get_object_or_404(CustomUser,id=request.user.pk)
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.project=post
            comment.user=user
            comment.save()
            return redirect('post_detail',slug=slugs)

class UpdateComment(UpdateView):
    template_name = "comments/update_comment.html"
    model = Comment
    permission_classes = [IsOwnerOrReadOnly,IsAuthenticatedOrReadOnly]
    form_class = CommentForm
    success_url = reverse_lazy('post_list')

class DeleteComment(DeleteView):
    template_name="comments/delete_comment.html"
    model = Comment
    permission_classes = [IsOwnerOrReadOnly,IsAuthenticatedOrReadOnly]
    success_url = reverse_lazy('post_list')


class CommentDetailView(DetailView):
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        context={}
        post_slug=kwargs.get('slug',"no slug")
        slugs=kwargs.get('pk',"no id")
        comment=get_object_or_404(Comment,id=slugs)
        context['comments']=comment
        form=CommentForm2()
        context['form']=form
        context['post_slug']=post_slug

        return render(request,'comments/comment_detail.html',context)

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        slugs=kwargs.get('pk',"no id")
        project=kwargs.get('slug',"no slug")
        comment=get_object_or_404(Comment,id=slugs)
        user=get_object_or_404(CustomUser,id=request.user.pk)
        form=CommentForm2(request.POST)
        if form.is_valid():
            chiled_comment=form.save(commit=False)
            chiled_comment.parent_comment=comment
            chiled_comment.user=user
            chiled_comment.save()

            return redirect('comment_detail',slug=project,pk=comment.id)


class UpdateChildComment(UpdateView):
    template_name = "comments/update_comment.html"
    model = ChildComment
    permission_classes = [IsOwnerOrReadOnly,IsAuthenticatedOrReadOnly]
    form_class = CommentForm2
    success_url = reverse_lazy('post_list')

class DeleteChildComment(DeleteView):
    template_name="comments/delete_comment.html"
    model = ChildComment
    permission_classes = [IsOwnerOrReadOnly,IsAuthenticatedOrReadOnly]
    success_url = reverse_lazy('post_list')
