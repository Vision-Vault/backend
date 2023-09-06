from django.urls import path
from .views import PostListView
from comments.views import CommentDetailView,PostDetailView,UpdateComment,UpdateChildComment,DeleteComment,DeleteChildComment


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path("<slug:slug>/",PostDetailView.as_view(),name="post_detail"),
    path("<slug:slug>/<int:pk>/",CommentDetailView.as_view(),name="comment_detail"),
    path("<slug:slug>/<int:pk>/update",UpdateComment.as_view(),name="update_comment"),
    path("<slug:slug>/<int:pk>/delete",DeleteComment.as_view(),name='delete_comment'),
    path("<slug:slug>/<int:id>/<int:pk>/update",UpdateChildComment.as_view(),name='update_coment_child'),
    path("<slug:slug>/<int:id>/<int:pk>/delete",DeleteChildComment.as_view(),name='delete_child_comment')
]
