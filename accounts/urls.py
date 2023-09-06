from django.urls import path
from .views import profile_view , update_profile, delete_profile


urlpatterns = [
    path('<int:pk>/', profile_view, name='profile'),
    path('<int:pk>/update/',update_profile, name='update_profile'),
    path('<int:pk>/delete/', delete_profile, name='delete_profile'),

]
