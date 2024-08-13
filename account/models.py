from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Man'),
        ('W', 'Woman'),
    ]

    gender = models.CharField(default='M', choices=GENDER_CHOICES, max_length=1)
    job = models.CharField(max_length=200)
    image = models.ImageField(upload_to='cover/profile/', blank=True)
    
    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        if self.image is None:
            if self.gender == 'M':
                self.image = '/static/img/card2.png'
            else:
                self.image = '/static/img/card1.png'
        return super().save(*args, **kwargs)


