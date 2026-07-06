from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('listener', 'Listener'),
        ('curator', 'Curator'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='listener')

    def is_curator(self):
        return self.role == 'curator'

    def __str__(self):
        return self.username

# Create your models here.
