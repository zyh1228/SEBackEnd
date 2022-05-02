from django.apps import apps
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(openid=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, openid, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(openid, email, password, **extra_fields)

    def create_superuser(self, openid, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(openid, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    openid = models.TextField(unique=True)
    nick_name = models.TextField()
    email = models.TextField(null=True)
    phone = models.TextField(max_length=11, null=True)
    avatar_url = models.TextField()
    gender = models.TextField(max_length=1, default='0')

    create_time = models.DateTimeField(auto_now_add=True, null=True)
    # admin_type = models.TextField(default=AdminType.REGULAR_USER)
    session_key = models.TextField(default='')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "openid"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = "user"
