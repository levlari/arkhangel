# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    #fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('answers','isComplit','points','curent_question')}),)
    fieldsets = ((None, {'fields': ('username', 'answers', 'curent_test', 'points', 'curent_question')}),)
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'answers','curent_test','points']

admin.site.register(CustomUser, CustomUserAdmin)
