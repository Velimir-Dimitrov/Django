from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from FiTrack.accounts.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    objects = AppUserManager()

    USERNAME_FIELD = "email"

    email = models.EmailField(
        unique=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )



