from django.urls import path
from . import views

urlpatterns = [
    path("", views.write_description, name="write_description"),
    path("", views.carousel_view, name="carousel_view"),
]
