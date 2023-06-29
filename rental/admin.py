from django.contrib import admin
from .models import CarCategory, Booking

@admin.register(CarCategory)
class CarCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'base_day_rental', 'kilometer_price')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'car_category', 'rental_datetime', 'return_datetime', 'total_amount')
