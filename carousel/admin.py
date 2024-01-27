from django.contrib import admin
from carousel.models import CarouselItem

class CarouselItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(CarouselItem, CarouselItemAdmin)