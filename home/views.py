from django.shortcuts import render
from home.models import MainPicture

def home(request):
    image = MainPicture.objects.first()
    context = {
        "main_ilustration" : image,
        }

    return render(request, 'home/home.html', context) 
