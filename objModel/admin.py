from django.contrib import admin

from objModel.models import Category, ObjModel


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'create_time', 'last_edit_time', 'created_by']
    search_fields = ['category_name', ]
    list_filter = ['create_time', 'last_edit_time', 'created_by']


class ObjModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'file_type', 'category', 'visible', 'create_time', 'last_edit_time', 'created_by']
    search_fields = ['name', 'description']
    list_filter = ['create_time', 'last_edit_time', 'file_type', 'visible', 'created_by']


admin.site.register(Category, CategoryAdmin)
admin.site.register(ObjModel, ObjModelAdmin)

