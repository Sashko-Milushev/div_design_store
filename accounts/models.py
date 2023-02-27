from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    NAME_MAX_LEN = 30
    email = models.EmailField(
        verbose_name='Email',
        unique=True,
        null=False,
        blank=False
    )
    first_name = models.CharField(
        verbose_name='First Name',
        max_length=NAME_MAX_LEN,
        null=False,
        blank=True,
        default='---'
    )
    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=NAME_MAX_LEN,
        null=False,
        blank=True,
        default='---'
    )
    date_joined = models.DateTimeField(
        verbose_name='Date Joined',
        auto_now_add=True,
        null=False,
        blank=False
    )
    is_active = models.BooleanField(
        verbose_name='Active',
        default=True,
        null=False,
        blank=False
    )

    objects = UserManager()

    # Users will register and log in the site with their email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    # TODO: implement send mail
    # def email_user(self):
    #     send_mail(subject, message, from_email, self.email, **kwargs)