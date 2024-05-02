from djmoney.models.fields import MoneyField
from django.db import models

# Create your models here.
class Delivery(models.Model):
    product_name = models.CharField(max_length=1024)
    price = MoneyField(max_digits=19, decimal_places=4, default_currency='PLN')
    