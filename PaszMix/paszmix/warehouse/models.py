from djmoney.models.fields import MoneyField
from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=1024)
    #params
    #Lizyna, Metionina, Metionina+cystyna, Treonina, Tryptofan, Arginina, Walina, Izoleucyna, Białko ogólne, Wapń, Fosfor_przyswajalny, Sód, kwas_linolowy 

class Delivery(models.Model):
    product_name = models.CharField(max_length=1024)
    price = MoneyField(max_digits=19, decimal_places=4, default_currency='PLN')
    date = models.DateTimeField
    initial_quantity = models.FloatField()
    used_quantity = models.FloatField()
    waste = models.FloatField()
    is_finished = models.BooleanField()