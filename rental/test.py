from django.test import TestCase
from django.utils import timezone
from .models import CarCategory, Rental, Return

class RentalTests(TestCase):
    def setUp(self):
        self.compact_category = CarCategory.objects.create(name='compact', base_day_rental=50, kilometer_price=10)
        self.premium_category = CarCategory.objects.create(name='premium', base_day_rental=50, kilometer_price=10)
        self.minivan_category = CarCategory.objects.create(name='minivan', base_day_rental=50, kilometer_price=10)

        self.rental = Rental.objects.create(
            booking_number='ABC123',
            customer_name='John Doe',
            car_category=self.compact_category,
            rental_datetime=timezone.now(),
            car_mileage=1000
        )

        self.car_return = Return.objects.create(
            rental=self.rental,
            return_datetime=timezone.now(),
            mileage_at_return=10500
        )

    def test_rental_price_calculation_compact(self):
        price = self.car_return.calculate_price()
        self.assertEqual(price, 500)  # 5 days * $50/day = $250

    def test_rental_price_calculation_premium(self):
        self.rental.car_category = self.premium_category
        self.rental.save()
        price = self.car_return.calculate_price()
        self.assertEqual(price, 620)  # 5 days * $80/day + 500 km * $0.2/km = $400 + $100 = $500

    def test_rental_price_calculation_minivan(self):
        self.rental.car_category = self.minivan_category
        self.rental.save()
        price = self.car_return.calculate_price()
        self.assertEqual(price, 1005)  # 5 days * $100/day + 500 km * $0.3/km * 1.5 = $500 + $225 = $725


class RentalModelTests(TestCase):
    def test_get_rental_days(self):
        rental = Rental(rental_datetime=timezone.now())
        rental.rental_datetime -= timezone.timedelta(days=3)
        rental.save()

        days = rental.get_rental_days()
        self.assertEqual(days, 3)

    def test_get_total_kilometers(self):
        rental = Rental(car_mileage=10000)
        return_obj = Return(mileage_at_return=10500, rental=rental)

        kilometers = return_obj.get_total_kilometers()
        self.assertEqual(kilometers, 500)


class CarCategoryModelTests(TestCase):
    def test_car_category_str(self):
        category = CarCategory(name='Compact')
        self.assertEqual(str(category), 'Compact')
