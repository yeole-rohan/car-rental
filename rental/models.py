from django.db import models
from django.core.exceptions import ValidationError

class CarCategory(models.Model):
    CATEGORY = (
        ('compact', 'Compact'),
        ('premium', 'Premium'),
        ('minivan', 'Minivan'),
    )
    name = models.CharField(max_length=50, choices=CATEGORY)
    base_day_rental = models.PositiveIntegerField(("base rental Day"), default=50)
    kilometer_price = models.FloatField(("Kilometer Price"), default=10)
    def __str__(self):
        return self.name


class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    car_category = models.ForeignKey(CarCategory, on_delete=models.CASCADE)
    rental_datetime = models.DateTimeField(help_text="Format yyyy-mm-dd hh:mm::ss")
    return_datetime = models.DateTimeField(blank=True,null=True, help_text="Format yyyy-mm-dd hh:mm::ss")
    car_mileage_at_pickup = models.IntegerField(default=0)
    car_mileage_at_return = models.IntegerField(default=0)
    total_amount = models.FloatField(("Total Car Booking Amount"), default=0.0)

    @property
    def calculate_price(self):
        if self.car_category.name == 'compact':
            price = self.car_category.base_day_rental * self.get_rental_days()
        elif self.car_category.name == 'premium':
            price = self.car_category.base_day_rental * self.get_rental_days() * 1.2
            price += self.car_category.kilometer_price * self.get_total_kilometers()
        elif self.car_category.name == 'minivan':
            price = self.car_category.base_day_rental * self.get_rental_days() * 1.7
            price += self.car_category.kilometer_price * self.get_total_kilometers() * 1.5
        else:
            raise ValueError("Invalid car category")

        return price

    def get_rental_days(self):
        return (self.return_datetime - self.rental_datetime).days

    def get_total_kilometers(self):
        return self.car_mileage_at_return - self.car_mileage_at_pickup
    
    def clean(self):
        if self.return_datetime and self.return_datetime < self.rental_datetime:
            raise ValidationError("Return date/time cannot be earlier than rental date/time.")
        
        if not self.car_mileage_at_return == 0 and self.car_mileage_at_return <= self.car_mileage_at_pickup:
            raise ValidationError("Car mileage at return must be greater than car mileage at pickup.")
            
    def __str__(self):
        return str(self.id)