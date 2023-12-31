# Generated by Django 4.2.2 on 2023-06-28 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carcategory',
            name='base_day_rental',
            field=models.PositiveIntegerField(default=50, verbose_name='base rental Day'),
        ),
        migrations.AddField(
            model_name='carcategory',
            name='kilometer_price',
            field=models.FloatField(default=10, verbose_name='Kilometer Price'),
        ),
    ]
