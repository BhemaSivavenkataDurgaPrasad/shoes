from django.db import models

# Create your models here.

class ShoesList(models.Model):
    brand = models.CharField(max_length=125)
    size = models.IntegerField(default = 6)
    price = models.IntegerField(default = 250)

    def __str__(self):
        return self.brand