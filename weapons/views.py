from django.shortcuts import render
from weapons.models import Weapon

def weapon_index(request):
    weapons = Weapon.objects.all()
    context = {
        "weapons": weapons    
    }
    return render(request, "weapons/weapons_index.html", context)

def weapon_detail(request, pk):
    weapons = Weapon.objects.get(pk=pk)
    context = {
        "weapons": weapons    
    }
    return render(request, "weapons/weapons_index.html", context)