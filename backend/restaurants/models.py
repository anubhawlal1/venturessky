from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=200, unique=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=20, unique=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-rating']
