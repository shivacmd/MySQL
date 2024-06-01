from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from core.models import TimestampModel
from core.common import MOBILE_REGEX


class CustomUserManager(BaseUserManager):

    def create_user(self, mobile_number, password, **extrafields):
        if not mobile_number:
            raise ValueError('Mobile number is must.')
        user = self.model(mobile_number=mobile_number, **extrafields)
        user.set_password(password)
        user.save()
        return user 

    def create_superuser(self, mobile_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(mobile_number, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin, TimestampModel):
    username = models.CharField(max_length=150, null=False, blank=False)
    email = models.CharField(max_length=255, null=False, blank=False)
    mobile_number = models.CharField(max_length=10, unique=True, validators=[MOBILE_REGEX])
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.mobile_number
    

