from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    user_type = models.CharField(
        max_length=20,
        choices=[('Admin', 'Administrador'), ('Reader', 'Leitor')],
        default='Reader'
    )
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return self.full_name