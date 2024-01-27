from django.shortcuts import render
from description.models import Description

def write_description(request):
    description_text = Description.objects.all().values()
    context = {
        "description_text": description_text,
    }
    return render(request, "description/index.html", context)