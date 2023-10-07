from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


class User(AbstractUser):
    username = None
    name = models.CharField(max_length=100)
    email = models.EmailField(_('email address'), unique=True)

    CHOICES = [
        ('D', 'doctor'),
        ('P', 'patient')
    ]
    role = models.CharField(max_length=20, choices=CHOICES, default='P')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'role']

    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')


    objects = UserManager()

    def __str__(self) -> str:
        return self.email