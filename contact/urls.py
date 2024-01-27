from django.urls import path
from contact import views

urlpatterns = [
    path("", views.get_contact, name="get_contact"),    
]