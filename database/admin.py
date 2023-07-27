from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    # List of fields to display in the user change list
    list_display = ('email', 'username', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_active', 'is_staff', 'is_superuser')

    # Add any other customizations as needed, e.g., search_fields, list_filter, etc.

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)