from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, username, first_name, password=None,  **other_fields):
        user = self.model(username=username, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)

        return self.create_user(username=username, first_name='Admin', password=password, **other_fields)


class AdhoUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    mobile_number = models.CharField(max_length=50, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    country = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=50, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
