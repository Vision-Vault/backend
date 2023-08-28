from django.urls import path
from .views import PostListView
from comments.views import CommentDetailView,PostDetailView


urlpatterns = [
    path('', PostListView.as_view(), name='post_detail'),
    path("<slug:slug>/",PostDetailView.as_view(),name="post_detail"),
    path("<slug:slug>/<int:pk>/",CommentDetailView.as_view(),name="comment_detail")
]
