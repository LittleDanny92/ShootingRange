from django.db import models

class WeaponType(models.Model):
    weapon_type = models.CharField(max_length=50)

    def __str__(self):
        return self.weapon_type

class Weapon(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=150)
    caliber = models.CharField(max_length=50)
    description = models.TextField()
    image = models.FileField(upload_to="weapons_images", blank=True)
    weapon_types = models.ManyToManyField("WeaponType", related_name="weapons")

    def __str__(self):
        return self.model
