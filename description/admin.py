from django.contrib import admin
from description.models import Description

class DescriptionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Description, DescriptionAdmin)
