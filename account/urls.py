from django.urls import path

from .views import UserAPI, UserLoginAPI, UserLogoutAPI


urlpatterns = [
    path('user', UserAPI.as_view(), name='user_api'),
    path('user/login', UserLoginAPI.as_view(), name='user_login_api'),
    path('user/logout', UserLogoutAPI.as_view(), name='user_logout_api'),
]
