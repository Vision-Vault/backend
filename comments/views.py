from .models import Comment,ChildComment
from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView
from .form import CommentForm,CommentForm2
from posts.models import Post
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
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('post_detail',slug=slugs)

class CommentDetailView(DetailView):
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        context={}
        slugs=kwargs.get('id',"no id")
        comment=get_object_or_404(Comment,id=slugs)
        context['comment']=comment
        form=CommentForm2()
        context['form']=form

        return render(request,'comments/comment_detail.html',context)

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        slugs=kwargs.get('id',"no id")
        comment=get_object_or_404(Comment,id=slugs)
        form=CommentForm(request.POST)
        if form.is_valid():
            chiled_comment=form.save(commit=False)
            chiled_comment.comment=comment
            chiled_comment.save()
            return redirect('comment_detail',id=slugs)
