from django.shortcuts import render, get_object_or_404, redirect
from .models import CustomUser
from .forms import UserProfileForm
from django.urls import reverse


def profile_view(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    return render(request, 'account/profile.html', {'user': user})

def update_profile(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=user.pk)
    else:
        form = UserProfileForm(instance=user)

    return render(request, 'account/update_profile.html', {'form': form, 'user': user})

def delete_profile(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)

    if request.method == 'POST':
        user.delete()
        return redirect(reverse('post_detail'))

    return render(request, 'account/delete_profile.html', {'user': user})
