from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        user = self.model(email = email, **kwargs)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(email=email)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user


class User(AbstractBaseUser, BaseModel):
    email = models.CharField(max_length=50, verbose_name="Адрес электронной почты.",unique = True)
    full_name = models.CharField(max_length = 100, verbose_name = "ФИО пользователя.")
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)
    USERNAME_FIELD = 'email'
    objects = UserManager()