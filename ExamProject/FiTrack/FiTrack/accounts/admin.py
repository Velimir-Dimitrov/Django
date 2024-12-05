from django.contrib import admin
from unfold.admin import ModelAdmin
from django.contrib.auth import get_user_model

from FiTrack.accounts.forms import AppUserCreationForm, AppUserChangeForm
from FiTrack.accounts.models import Profile

UserModel = get_user_model()


class ProfileInline(admin.TabularInline):
    model = Profile
    can_delete = False
    verbose_name = "Personal Information"


@admin.register(UserModel)
class AppUserAdmin(ModelAdmin):
    model = UserModel
    add_form = AppUserCreationForm
    form = AppUserChangeForm
    inlines = (ProfileInline,)


    list_display = ('pk', 'email', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    list_filter = ('is_staff', "is_superuser")
    ordering = ('pk',)

    fieldsets = (
        ('Account credentials', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
