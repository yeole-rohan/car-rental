# Generated by Django 4.2.2 on 2023-06-29 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_carcategory_base_day_rental_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('rental_datetime', models.DateTimeField()),
                ('return_datetime', models.DateTimeField()),
                ('car_mileage_at_pickup', models.IntegerField()),
                ('car_mileage_at_return', models.IntegerField()),
                ('car_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.carcategory')),
            ],
        ),
        migrations.RemoveField(
            model_name='return',
            name='rental',
        ),
        migrations.DeleteModel(
            name='Rental',
        ),
        migrations.DeleteModel(
            name='Return',
        ),
    ]
