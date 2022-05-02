from django.urls import path

from .views import UserAPI, UserLogoutAPI


urlpatterns = [
    path('user', UserAPI.as_view(), name='user_api'),
    path('user/login', UserLogoutAPI.as_view(), name='user_logout_api')
]
