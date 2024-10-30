from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'user_type', 'address', 'phone')
    search_fields = ('full_name', 'email', 'user_type')
    list_filter = ('user_type',)

admin.site.register(User, UserAdmin)