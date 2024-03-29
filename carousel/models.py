from django.db import models

class CarouselItem(models.Model):
    image = models.ImageField(upload_to='carousel_images/')
    caption = models.CharField(max_length=255, blank = True)

    def __str__(self):
        return self.caption
