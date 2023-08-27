from django.shortcuts import render, get_object_or_404
from .models import CustomUser

def profile_view(request, slug):  
    user = get_object_or_404(CustomUser, slug=slug)
    return render(request, 'account/profile.html', {'user': user})
