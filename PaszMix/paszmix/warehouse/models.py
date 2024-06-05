from djmoney.models.fields import MoneyField
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

#https://stackoverflow.com/questions/36477759/django-percentage-field
PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

class Product(models.Model):
    product_name = models.CharField(max_length=1024)
    #params
    wilgotnosc = models.DecimalField(max_digits=3, decimal_places=0, default=12, validators=PERCENTAGE_VALIDATOR)
    bialko_ogolne = 
    #Lizyna, Metionina, Metionina+cystyna, Treonina, Tryptofan, Arginina, Walina, Izoleucyna, Białko ogólne, Wapń, 
    #Fosfor_przyswajalny, Sód, kwas_linolowy 

class Delivery(models.Model):
    product_name = models.CharField(max_length=1024)
    price = MoneyField(max_digits=19, decimal_places=4, default_currency='PLN')
    date = models.DateTimeField
    initial_quantity = models.FloatField()
    used_quantity = models.FloatField()
    waste = models.FloatField()
    is_finished = models.BooleanField()