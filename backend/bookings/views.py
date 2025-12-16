from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from users import decorators
from django.db import transaction
from users.decorators import patient_required

# from users.decorators import doctor_required
from .models import AvailabilitySlot

# Create your views here.

@login_required
@decorators.doctor_required
def add_availability(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        AvailabilitySlot.objects.create(
            doctor=request.user,
            date=date,
            start_time=start_time,
            end_time=end_time
        )

        return redirect('doctor-slots')

    return render(request, 'bookings/add_availability.html')


@login_required
@decorators.doctor_required
def doctor_slots(request):
    slots = AvailabilitySlot.objects.filter(
        doctor=request.user,
        date__gte=timezone.now().date()
    )

    return render(request, 'bookings/doctor_slots.html', {'slots': slots})


@login_required
@patient_required
def available_slots(request):
    slots = AvailabilitySlot.objects.filter(
        is_booked=False,
        date__gte=timezone.now().date()
    ).select_related('doctor')

    return render(request, 'bookings/available_slots.html', {'slots': slots})


@login_required
@patient_required
def book_slot(request, slot_id):
    with transaction.atomic():
        slot = AvailabilitySlot.objects.select_for_update().get(id=slot_id)

        if slot.is_booked:
            return render(request, 'bookings/already_booked.html')

        slot.is_booked = True
        slot.save()

    return render(request, 'bookings/booking_success.html', {'slot': slot})
