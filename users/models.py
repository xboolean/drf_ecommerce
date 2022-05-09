from django.db import models
from django.utils import timezone
from base.models import BaseModel
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError(_('Users must have an email address'))
        user = self.model(email = email, **kwargs)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(email=email)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user


class User(AbstractBaseUser, BaseModel, PermissionsMixin):
    email = models.CharField(max_length=50, verbose_name="Адрес электронной почты.", unique = True)
    full_name = models.CharField(max_length = 100, verbose_name = "ФИО пользователя.")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label) -> bool:
        return self.is_superuser
	
    def has_perm(self, perm, obj=None) -> bool:
        if perm in self.get_all_permissions():
            return True
        return self.is_superuser