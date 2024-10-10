from django.db import models

class MainPicture(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to="mainpage_images", blank=True)

    def __str__(self):
        return self.name
