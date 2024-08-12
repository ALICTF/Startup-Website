from django.db import models


class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    # image = models.ImageField(upload_to='cover/portfolio/')
    
    def __str__(self):
        return self.name
