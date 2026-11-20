from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (('Extra', {'fields': ('phone',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (('Extra', {'fields': ('email', 'phone')}),)
