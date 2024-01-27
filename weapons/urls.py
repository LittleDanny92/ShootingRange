from django.urls import path
from weapons import views

urlpatterns = [
    path("", views.weapon_index, name="weapon_index"),
]