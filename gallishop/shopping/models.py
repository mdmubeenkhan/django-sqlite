from django.db import models
from django.urls import reverse

# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=10)
    price = models.FloatField()
    quantity = models.IntegerField()

    def get_absolute_url(self):
        return reverse('details')