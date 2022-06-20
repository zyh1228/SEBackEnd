from django.contrib import admin

from history.models import History


class HistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by', 'obj_model', 'view_time', 'view_count']
    search_fields = ['obj_model', ]
    list_filter = ['view_time', 'created_by']


admin.site.register(History, HistoryAdmin)
