from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
    date_expired = models.DateField(auto_now_add=True)
    amount = models.IntegerField()


