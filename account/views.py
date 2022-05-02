import requests
from django.contrib import auth
from rest_framework.views import APIView
from utils.api.api import APIView, validate_serializer
from seBackEnd.settings import APP_ID, APP_SECRET
from account.serializers import UserLoginSerializer, UserSerializer, UserEditSerializer
from account.models import User


def get_openid(code):
    url = 'https://api.weixin.qq.com/sns/jscode2session' + "?appid=" + APP_ID + "&secret=" + APP_SECRET + \
          "&js_code=" + code + "&grant_type=authorization_code"
    res = requests.get(url)
    openid = res.json().get('openid')
    session_key = res.json().get('session_key')
    return openid, session_key


class UserAPI(APIView):

    @validate_serializer(UserLoginSerializer)
    def post(self, request):
        code = request.data.get('code')
        nick_name = request.data.get('nick_name')
        avatar_url = request.data.get('avatar_url')

        openid, session_key = get_openid(code)
        if openid is None:
            return self.error('code error')
        if not User.objects.filter(openid=openid).exists():
            user = User.objects.create(openid=openid, nick_name=nick_name, avatar_url=avatar_url)
            user.is_active = True
            user.set_password(openid)
            user.save()

        user = auth.authenticate(username=openid, password=openid)
        if user:
            auth.login(request, user)
            return self.success()
        else:
            return self.error('authentication failed')

    def get(self, request):
        user = request.user
        return self.success(UserSerializer(user).data)

    @validate_serializer(UserEditSerializer)
    def put(self, request):
        data = request.data
        user = request.user

        for key, value in data.items():
            if value:
                setattr(user, key, value)
        user.save()

        return self.success(UserSerializer(user).data)

    def delete(self, request):
        user = request.user
        auth.logout(request)
        user.delete()
        return self.success()


class UserLogoutAPI(APIView):
    def get(self, request):
        auth.logout(request)
        return self.success()
