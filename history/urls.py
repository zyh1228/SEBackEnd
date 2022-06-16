from django.urls import path

from history.views import HistoryAPI


urlpatterns = [
    path('history', HistoryAPI.as_view(), name='history_api'),
]
