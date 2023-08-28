from .models import Comment,ChildComment
from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView
from .form import CommentForm,CommentForm2
from posts.models import Post
from accounts.models import CustomUser
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

class CommentDetailView(DetailView):
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        context={}
        print(kwargs)
        slugs=kwargs.get('pk',"no id")
        comment=get_object_or_404(Comment,id=slugs)
        context['comment']=comment
        form=CommentForm2()
        context['form']=form

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
