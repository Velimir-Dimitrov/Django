from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from petstagram.accounts.managers import AppUserManager


# Create your models here.

class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True
    )

    is_active = models.BooleanField(
        default=True
    )

    is_staff = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AppUserManager()

    def __str__(self):
        return self.email

