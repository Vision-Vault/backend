from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import UserProfileForm

class CustomUserAdmin(UserAdmin):
    add_form = UserProfileForm
    form = UserProfileForm
    model = CustomUser
    list_display = ('username', 'first_name', 'last_name', 'email', 'profile_picture')
    fieldsets = (
        (None, {'fields': ('username', 'password', 'first_name', 'last_name', 'email')}),
        ('Profile Information', {'fields': ('profile_picture', 'bio')}),
        ('User permissions',{
            'fields':('is_staff','is_superuser')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password', 'first_name', 'last_name', 'email', 'profile_picture', 'bio','is_staff','is_superuser' ),
        }),
    )
    ordering = ('username',)  # Specify the default ordering

admin.site.register(CustomUser, CustomUserAdmin)
