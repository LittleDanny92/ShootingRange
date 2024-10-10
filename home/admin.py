from django.contrib import admin
from home.models import MainPicture

class MainPictureAdmin(admin.ModelAdmin):
    pass

admin.site.register(MainPicture, MainPictureAdmin)

