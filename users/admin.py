from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    fieldsets = ((None, {'fields': ('username',
                                    'answers',
                                    'curent_test',
                                    'points',
                                    'curent_question',
                                    'time_begin',
                                    'date_begin'
                                    )}),)
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'answers', 'curent_test', 'points']


admin.site.register(CustomUser, CustomUserAdmin)
