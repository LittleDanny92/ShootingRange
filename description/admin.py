from django.contrib import admin
from description.models import Description,CarouselItem

class DescriptionAdmin(admin.ModelAdmin):
    pass

class CarouselItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Description, DescriptionAdmin)
admin.site.register(CarouselItem, CarouselItemAdmin)