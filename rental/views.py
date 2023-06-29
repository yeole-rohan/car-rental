from django.shortcuts import render, redirect
from .forms import RegistrationForm, ReturnForm
from .models import Booking

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rental:car_list')  
    else:
        form = RegistrationForm()
    
    return render(request, 'register-car.html', {'form': form})

def car_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking-list.html', {'bookings': bookings})

def return_car(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if request.method == 'POST':
        form = ReturnForm(request.POST or None, instance=booking)
        if form.is_valid():
            form = form.save(commit=False)
            form.total_amount = booking.calculate_price
            form.save()
            return redirect('rental:car_list')
    else:
        form = ReturnForm(instance=booking)
    return render(request, 'return-car.html', {'booking' : booking, 'form' : form})