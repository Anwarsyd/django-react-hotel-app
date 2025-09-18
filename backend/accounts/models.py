from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    guest_type = models.CharField(
        max_length=10,
        choices=[('regular', 'Regular'), ('vip', 'VIP')],
        default='regular'
    )
    face_encoding = models.TextField(blank=True)
    is_active_guest = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.username} ({self.guest_type})"
