from django.db import models


class SortByDateTime(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('name')


class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    # image = models.ImageField(upload_to='cover/portfolio/')

    objects = SortByDateTime()
    
    def __str__(self):
        return self.name
