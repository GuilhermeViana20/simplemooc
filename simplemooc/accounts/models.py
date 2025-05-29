import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Nome de Usuário', max_length=30, unique=True,
        validators=[validators.RegexValidator(re.compile(r'^[\w.@+-]+$'),
        'O nome de usuário só pode conter letras, números e os seguintes caracteres: @/./+/-/_.',
        'invalid'
    )]
    )
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome', max_length=30, blank=True)
    surname = models.CharField('Sobrenome', max_length=30, blank=True)
    is_active = models.BooleanField('Ativo', blank=True, default=True)
    is_staff = models.BooleanField('Membro da Equipe', blank=True, default=False)
    date_joined = models.DateTimeField('Data de Registro', auto_now_add=True)
    image = models.ImageField('Imagem', upload_to='profile_pics/', blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username
    
    def get_shot_name(self):
        return self.username
    
    def get_full_name(self):
        if self.name and self.surname:
            return f'{self.name} {self.surname}'
        return self.username
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['username']