from django.urls import path
from reservation_form import views

urlpatterns = [
    path("", views.visit_booking, name="visit_booking"),
    path("get_available_times/", views.get_available_times, name="get_available_times"),
]