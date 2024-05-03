from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

from .models import CustomUser, Profile

class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    
    list_display = ["username","email","is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        ("User", {"fields": ["username","email","first_name","last_name","password"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["username", "email", "first_name","last_name","password1","password2"],    
            },
        ),
    ]
    search_fields = ["username"]
    ordering = ["username"]
    filter_horizontal = []

# Unregister the Group model from admin.
admin.site.unregister(Group)

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Profile)