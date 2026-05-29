from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display  = ('username', 'email', 'role', 'matricule', 'is_active')
    list_filter   = ('role', 'is_active')
    search_fields = ('username', 'email', 'matricule')

    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {
            'fields': ('role', 'matricule')
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Info', {
            'fields': ('role', 'matricule')
        }),
    )