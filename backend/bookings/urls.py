from django.urls import path
from .views import add_availability, doctor_slots

urlpatterns = [
    path('doctor/add-slot/', add_availability, name='add-availability'),
    path('doctor/slots/', doctor_slots, name='doctor-slots'),
]
