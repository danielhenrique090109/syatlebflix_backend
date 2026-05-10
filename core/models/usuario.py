from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    foto_perfil = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, default='ativo')
    email = models.EmailField(unique=True)
    # nome → primeiro_nome/last_name já vêm do AbstractUser
    # email → já vem do AbstractUser
    # senha → já vem como password com hash automático
    # data_criacao → já vem como date_joined

def __str__(self):
        return self.email