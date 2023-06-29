from django import forms
from django.core.exceptions import ValidationError
from .models import Booking

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ("car_mileage_at_return", "return_datetime", "total_amount")
    
    def clean(self):
        category = self.cleaned_data.get("car_category")
        if Booking.objects.filter(car_category=category, total_amount=0).exists():
            raise ValidationError("Car Booking not available for this car.")

class ReturnForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ("car_mileage_at_return", "return_datetime")