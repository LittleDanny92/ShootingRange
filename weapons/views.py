from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from weapons.models import Weapon

def weapon_index(request):
    weapons = Weapon.objects.all()
    page = request.GET.get("page", 1)

    paginator = Paginator(weapons, 9)

    try:
        weapons = paginator.page(page)
    except PageNotAnInteger:
        weapons = paginator.page(1)
    except EmptyPage:
        weapons = paginator.page(paginator.num_pages)
    
    context = {
        "weapons": weapons    
    }
    return render(request, "weapons/weapons.html", context)
