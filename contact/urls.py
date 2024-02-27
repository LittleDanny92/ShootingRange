from django.urls import path
from contact import views

urlpatterns = [
    path("", views.leave_message, name="leave_message"),
]