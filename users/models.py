from django.db import models
import uuid
from django.utils import timezone
from django.conf import settings
from base.models import BaseModel
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db.models import Sum

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError(_('Users must have an email address'))
        user = self.model(email = email, **kwargs)
        user.set_password(password)

        user.save(using = self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(email=email, password=password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using = self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    uu_id = models.UUIDField(default=uuid.uuid4,  editable=False, unique=True)
    email = models.CharField(max_length=50, verbose_name="Адрес электронной почты.", unique = True)
    full_name = models.CharField(max_length = 100, verbose_name = "ФИО пользователя.")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
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

class CustomerProfile(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, to_field='uu_id', on_delete=models.CASCADE, related_name='profile')
    address = models.CharField(max_length=250)

    @property
    def cost_of_all_orders(self):
        self.orders.aggregate(Sum('order_price'))


