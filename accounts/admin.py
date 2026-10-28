from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'pecho_cm', 'cintura_cm', 'cadera_cm')
    list_filter = ('role',)
