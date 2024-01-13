from django.shortcuts import render
from description.models import Description, CarouselItem


def write_description(request):
    description_text = Description.objects.all().values()
    context = {
        "description_text": description_text,
    }
    return render(request, "description/index.html", context)

def carousel_view(request):
    carousel_items = CarouselItem.objects.all()
    context = {
        "carousel_item:": carousel_items
    }
    return render(request, "base.html", context)