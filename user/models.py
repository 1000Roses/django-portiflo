from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta
from django.conf import settings

import jwt


class CustomUser(AbstractUser):
    email = models.EmailField(('email address'), unique=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=150, null= True, blank=True)
    phone = models.CharField(max_length=10, blank=True, null=True, unique=True)
    description = models.TextField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    # because in default when create the superuser, username field is required
    REQUIRED_FIELDS = ['username']

    @property
    def access_token(self):
        token = jwt.encode({ 'id': self.id, 'type': 'access_token', 'username': self.first_name, 'email': self.email, 'exp': datetime.utcnow() + timedelta(days=1)}, settings.SECRET_KEY, algorithm= 'HS256')
        return token
    
    @property
    def refresh_token(self):
        token = jwt.encode({ 'id': self.id, 'type': 'refresh_token', 'username': self.first_name, 'email': self.email, 'exp': datetime.utcnow() + timedelta(days=27)}, settings.SECRET_KEY, algorithm= 'HS256')
        return token