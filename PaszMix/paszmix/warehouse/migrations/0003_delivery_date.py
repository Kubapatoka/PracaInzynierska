# Generated by Django 5.0.3 on 2024-07-03 14:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_production_rename_product_name_delivery_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 3, 14, 38, 1, 342723)),
        ),
    ]