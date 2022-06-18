from rest_framework import serializers

from account.models import User


class UserCreateOrLoginSerializer(serializers.Serializer):
    code = serializers.CharField()
    nick_name = serializers.CharField(max_length=1024)
    avatar_url = serializers.CharField()


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserEditSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=256, allow_null=True, allow_blank=True)
    phone = serializers.CharField(max_length=11, min_length=11, allow_null=True, allow_blank=True)

    def validate_phone(self, phone):
        start_num = phone[:2]
        if start_num not in [13, 14, 15, 16, 17, 18, 19]:
            raise serializers.ValidationError('请输入有效的手机号')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "nick_name", "email", "phone", "is_staff", "is_superuser", "create_time", "last_login"]


class UserNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "nick_name"]
