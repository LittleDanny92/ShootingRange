from django.shortcuts import render
from carousel.models import CarouselItem

def carousel_view(request):
    carousel_items = CarouselItem.objects.all()
    context = {
        "carousel_items": carousel_items,
    }
    return render(request, "carousel/carousel.html", context)
