from django.urls import path
from .views import PostListView
urlpatterns = [
    path('<str:status>/', PostListView.as_view(), name='post_detail')
]
