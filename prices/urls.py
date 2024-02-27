from django.urls import path
from prices import views

urlpatterns = [
    path("", views.get_prices, name="get_prices")    
]