from djmoney.models.fields import MoneyField
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
#from pgvector.django import VectorField
#https://github.com/pgvector/pgvector-python

#https://stackoverflow.com/questions/36477759/django-percentage-field
PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

class Product(models.Model):
    product_name = models.CharField(max_length=1024)
    #params
    wilgotnosc = models.DecimalField(max_digits=3, decimal_places=2, default=12, validators=PERCENTAGE_VALIDATOR)
    energia_metaboliczna = models.FloatField() 
    bialko_ogolne = models.DecimalField(max_digits=3, decimal_places=2, default=12, validators=PERCENTAGE_VALIDATOR)
    lizyna = models.FloatField()
    metionina = models.FloatField()
    cystyna = models.FloatField()
    treonina = models.FloatField()
    tryptofan = models.FloatField()
    arginina = models.FloatField()
    walina = models.FloatField()
    izoleucyna = models.FloatField()
    wapń = models.FloatField() 
    fosfor_przyswajalny = models.FloatField() 
    sod = models.FloatField()
    kwas_linolowy = models.FloatField() 


class Delivery(models.Model):
    product_name = models.ForeignKey(Product, models.CASCADE)
    price = MoneyField(max_digits=19, decimal_places=4, default_currency='PLN')
    date = models.DateTimeField
    initial_quantity = models.FloatField()
    used_quantity = models.FloatField()
    waste = models.FloatField()
    is_finished = models.BooleanField()


class Composition(models.Model):
    energia_metaboliczna_min = models.FloatField()
    energia_metaboliczna_max = models.FloatField()
    lizyna = models.FloatField()
    metionina = models.FloatField()
    cystyna_metionina = models.FloatField()
    treonina = models.FloatField()
    tryptofan = models.FloatField()
    arginina = models.FloatField()
    walina = models.FloatField()
    izoleucyna = models.FloatField()
    wapn = models.FloatField() 
    fosfor_przyswajalny = models.FloatField() 
    sod = models.FloatField()

# class Recipe(models.model):
#     mixture_list = VectorField()
