
from django.urls import path
from . import views
urlpatterns = [
    path("register/", views.register, name="register"),
    path("", views.car_list, name="car_list"),
    path("return/<int:booking_id>/", views.return_car, name="return_car"),
]
