from django.shortcuts import render
from prices.models import PriceList

def get_prices(request):
    prices = PriceList.objects.all()
    context = {
        "price_list_items": prices,    
    }

    return render(request, "prices/prices.html", context) 