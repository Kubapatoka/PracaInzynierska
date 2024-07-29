from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Delivery, Product, Composition, Production, Recipe

def index(request):
    latest_deliveries_list      = Delivery.objects.all()
    latest_products_list        = Product.objects.all()
    latest_compositions_list    = Composition.objects.all()
    latest_productions_list     = Production.objects.all()
    latest_recipes_list         = Recipe.objects.all()

    context = {
        "latest_deliveries_list": latest_deliveries_list,
        "latest_products_list": latest_products_list,
        "latest_compositions_list": latest_compositions_list,
        "latest_productions_list": latest_productions_list,
        "latest_recipes_list": latest_recipes_list,
    }
    return render(request, "warehouse/index.html", context)

def new_product(request):
    return HttpResponse("Tu będzie formularz do dodania nowego produktu")

def product(request, product_id):
    product = Product.objects.get(pk = product_id)
    context = {
        "product": product,
    }
    return render(request, "warehouse/product.html", context)

def new_delivery(request):
    return HttpResponse("Tu będzie formularz do dodania nowej dostawy")

def delivery(request, delivery_id):
    delivery = Delivery.objects.get(pk = delivery_id)
    context = {
        "delivery": delivery,
    }
    return render(request, "warehouse/delivery.html", context)

def new_recipe(request):
    return HttpResponse("Tu będzie formularz do dodania nowego przepisu")

def recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk = recipe_id)
    context = {
        "recipe": recipe,
    }
    return render(request, "warehouse/recipe.html", context)

def new_composition(request):
    return HttpResponse("tu będzie dodanie nowego składu")

def composition(request, composition_id):
    composition = Composition.objects.get(pk = composition_id)
    context = {
        "composition": composition,
    }
    return render(request, "warehouse/composition.html", context)

def new_production(request):
    return HttpResponse("tu będzie dodanie zlecenia produkcji")

def production(request, production_id):
    production = Production.objects.get(pk = production_id)
    context = {
        "production": production,
    }
    return render(request, "warehouse/production.html", context)

def stan_magazynowy(request):
    return HttpResponse("Tu będzie podawany akutalny stan magazynu, z podziałem na produkty i dostawy")

def archiwum_produkcji(request):
    return HttpResponse("Tu będzie archiwum zleceń produkcji")

def archiwum_dostaw(request):
    return HttpResponse("Tu będą dostawy chronologicznie, również te niezakończone")

def archiwum_dostaw_p(request, product_id):
    return HttpResponse("Tu będą wszystkie dostawy produktu: " + product_id + " uporządkowane chronologicznie")

def calculate_recipe(request, composition_id):
    return HttpResponse("Tu będzie można wyklikać recepturę na podstawie danego składu: " + composition_id)

def calculate_production(request, recipe_id):
    return HttpResponse("Tu będzie można utworzyć produkcje na podstawie konkretnej receptury: " + recipe_id)