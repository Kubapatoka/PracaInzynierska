from djmoney.models.fields import MoneyField
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone    
#from pgvector.django import VectorField
#https://github.com/pgvector/pgvector-python

#https://stackoverflow.com/questions/36477759/django-percentage-field
PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

class Product(models.Model):
    product_name = models.CharField(max_length=1024)
    #params
    wilgotnosc = models.DecimalField(max_digits=3, decimal_places=1, default=12, validators=PERCENTAGE_VALIDATOR)
    energia_metaboliczna = models.FloatField() 
    bialko_ogolne = models.DecimalField(max_digits=3, decimal_places=1, default=12, validators=PERCENTAGE_VALIDATOR)
    lizyna = models.FloatField()
    metionina = models.FloatField()
    cystyna = models.FloatField()
    treonina = models.FloatField()
    tryptofan = models.FloatField()
    arginina = models.FloatField()
    walina = models.FloatField()
    izoleucyna = models.FloatField()
    wapn = models.FloatField(default=0) 
    fosfor_przyswajalny = models.FloatField() 
    sod = models.FloatField()
    kwas_linolowy = models.FloatField()
    
    def __str__(self):
        return self.product_name


class Delivery(models.Model):
    product = models.ForeignKey(Product, models.CASCADE)
    price = MoneyField(max_digits=19, decimal_places=4, default_currency='PLN')
    date = models.DateTimeField(default=timezone.now)
    initial_quantity = models.FloatField()
    used_quantity = models.FloatField()
    waste = models.FloatField()
    is_finished = models.BooleanField()

    def __str__(self):
        result = self.product.__str__() + " " + self.date.__str__() + " " +  self.price + " " + self.initial_quantity.__str__()
        return result


class Composition(models.Model):
    composition_name = models.CharField(max_length=1024)
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

    def __str__(self):
        return self.composition_name



class Recipe(models.Model):
    composition = models.ForeignKey(Composition, models.SET_NULL, null= True, blank = True)
    name = models.CharField(max_length= 255)
    type = models.CharField(max_length= 255)


class RecipeElement(models.Model):
    recipe_ref = models.ForeignKey(Recipe, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)
    quantity = models.FloatField()

class Production(models.Model):
    recipe = models.ForeignKey(Recipe, models.SET_NULL, null= True)
    date = models.DateTimeField(default=timezone.now)
    name_of_final_product = models.CharField(max_length=255)

class ProductionElement(models.Model):
    production_ref = models.ForeignKey(Production, models.CASCADE)
    delivery_ref = models.ForeignKey(Delivery, models.CASCADE)
    quantity = models.FloatField()

