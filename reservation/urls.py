
from django.urls import path
from .views import ReservationPageView

app_name = "reservation" 

urlpatterns = [
    path("", ReservationPageView.as_view(), name = "reservation_form"),
]



