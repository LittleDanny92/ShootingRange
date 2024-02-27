from django.contrib import admin
from prices.models import PriceList

class PriceListAdmin(admin.ModelAdmin):
    pass

admin.site.register(PriceList, PriceListAdmin)
