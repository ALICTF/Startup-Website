from django.db import models
from django.contrib.auth.models import AbstractUser


# class CustomUser(AbstractUser):
#     GENDER_CHOICES = [
#         ('M', 'Man'),
#         ('W', 'Woman'),
#     ]

#     gender = models.CharField(default='M', choices=GENDER_CHOICES, max_length=1)
#     # image = models.ImageField(upload_to='cover/profile/')
    
#     def __str__(self):
#         return self.username


