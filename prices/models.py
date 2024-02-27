from django.db import models

class PriceList(models.Model):
    price_handgun = models.CharField(max_length=50)
    price_rifle = models.CharField(max_length=50)
    price_instructor = models.CharField(max_length=50)
    price_handgun_ammo = models.CharField(max_length=50)
    price_rifle_ammo = models.CharField(max_length=50)
    price_site = models.CharField(max_length=50)

    def __str__(self):
        return "Price List"

