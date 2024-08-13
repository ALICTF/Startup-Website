from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Man'),
        ('W', 'Woman'),
    ]

    gender = models.CharField(default='M', choices=GENDER_CHOICES, max_length=1)
    # job = models.CharField(max_length=200)
    # image = models.ImageField(upload_to='cover/profile/', blank=True)
    
    def __str__(self):
        return self.username


