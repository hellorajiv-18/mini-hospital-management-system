from django.urls import path
from .views import add_availability, doctor_slots, available_slots,book_slot

urlpatterns = [
    path('doctor/add-slot/', add_availability, name='add-availability'),
    path('doctor/slots/', doctor_slots, name='doctor-slots'),
    path('patient/slots/', available_slots, name='available-slots'),
    path('patient/book/<int:slot_id>/', book_slot, name='book-slot'),
]
