import requests
from django.contrib import auth

from account.decorators import login_required
from utils.api.api import APIView, validate_serializer
from seBackEnd.settings import APP_ID, APP_SECRET
from account.serializers import UserCreateOrLoginSerializer, UserLoginSerializer, UserSerializer, UserEditSerializer
from account.models import User


def get_openid(code):
    """向微信服务器换取openID

    :param code: 微信的code
    :return: openID, session_key
    """
    url = 'https://api.weixin.qq.com/sns/jscode2session' + "?appid=" + APP_ID + "&secret=" + APP_SECRET + \
          "&js_code=" + code + "&grant_type=authorization_code"
    res = requests.get(url)
    openid = res.json().get('openid')
    session_key = res.json().get('session_key')
    return openid, session_key


class UserAPI(APIView):
    """用户信息接口
    """

    @validate_serializer(UserCreateOrLoginSerializer)
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

    @login_required
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

    @login_required
    def delete(self, request):
        user = request.user
        auth.logout(request)
        user.delete()
        return self.success()


class UserLoginAPI(APIView):
    """登录接口，主要为了开发时测试方便
    """

    @validate_serializer(UserLoginSerializer)
    def post(self, request):
        """
        User login api
        """
        data = request.data
        user = auth.authenticate(username=data["username"], password=data["password"])
        if user:
            auth.login(request, user)
            return self.success("Succeeded")
        else:
            return self.error("Invalid username or password")


class UserLogoutAPI(APIView):
    """登出接口
    """

    @login_required
    def get(self, request):
        auth.logout(request)
        return self.success()
