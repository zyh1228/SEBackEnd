from django.contrib import admin

from account.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['nick_name', 'email', 'phone', 'gender', 'create_time', 'last_login', 'is_active', 'is_staff', 'is_superuser']
    search_fields = ['nick_name', 'email', 'phone']
    list_filter = ['create_time', 'last_login', 'is_active', 'is_staff', 'is_superuser']


admin.site.register(User, UserAdmin)
