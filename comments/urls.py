from django.urls import path
from .views import CommentDetailView,PostDetailView

urlpatterns = [
    path("<slug:slug>/",PostDetailView.as_view(),name="post_detail"),
    path("<int:pk>/",CommentDetailView.as_view(),name="comment_detail")
]
