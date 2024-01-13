from django.contrib import admin
from weapons.models import WeaponType, Weapon

class WeaponTypeAdmin(admin.ModelAdmin):
    pass

class WeaponAdmin(admin.ModelAdmin):
    pass

admin.site.register(WeaponType, WeaponAdmin)
admin.site.register(Weapon, WeaponAdmin)