from django.shortcuts import render, redirect
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
    latest_deliveries_list      = Delivery.objects.all()
    latest_products_list        = Product.objects.all()
    latest_compositions_list    = Composition.objects.all()
    latest_productions_list     = Production.objects.all()
    latest_recipes_list         = Recipe.objects.all()

    if request.method == "POST":
        product_name = request.POST.get('product_name')
        wilgotnosc = request.POST.get('wilgotnosc')
        energia_metaboliczna = request.POST.get('energia_metaboliczna')
        bialko_ogolne = request.POST.get('bialko_ogolne')
        lizyna = request.POST.get('lizyna')
        metionina = request.POST.get('metionina')
        cystyna = request.POST.get('cystyna')
        treonina = request.POST.get('treonina')
        tryptofan = request.POST.get('tryptofan')
        arginina = request.POST.get('arginina')
        walina = request.POST.get('walina')
        izoleucyna = request.POST.get('izoleucyna')
        wapn = request.POST.get('wapn')
        fosfor_przyswajalny = request.POST.get('fosfor_przyswajalny')
        sod = request.POST.get('sod')
        kwas_linolowy = request.POST.get('kwas_linolowy')

        if product_name != "":
            Product.objects.create(product_name=product_name, 
                                   wilgotnosc = wilgotnosc, 
                                   energia_metaboliczna = energia_metaboliczna, 
                                   bialko_ogolne = bialko_ogolne, 
                                   lizyna = lizyna,
                                   metionina = metionina, 
                                   cystyna = cystyna, 
                                   treonina = treonina, 
                                   tryptofan = tryptofan, 
                                   arginina = arginina, 
                                   walina = walina, 
                                   izoleucyna = izoleucyna, 
                                   wapn = wapn, 
                                   fosfor_przyswajalny = fosfor_przyswajalny, 
                                   sod = sod, 
                                   kwas_linolowy = kwas_linolowy)
            product = Product.objects.last()
            
            context = {
                "latest_deliveries_list": latest_deliveries_list,
                "latest_products_list": latest_products_list,
                "latest_compositions_list": latest_compositions_list,
                "latest_productions_list": latest_productions_list,
                "latest_recipes_list": latest_recipes_list,
                "product": product,
                "newly_created" : True,
                "readonly" : True
             }
            return render(request, "warehouse/product.html", context)

    context = {
        "latest_deliveries_list": latest_deliveries_list,
        "latest_products_list": latest_products_list,
        "latest_compositions_list": latest_compositions_list,
        "latest_productions_list": latest_productions_list,
        "latest_recipes_list": latest_recipes_list,
    }
    return render(request, "warehouse/add_product.html", context)

def product(request, product_id):
    latest_deliveries_list      = Delivery.objects.all()
    latest_products_list        = Product.objects.all()
    latest_compositions_list    = Composition.objects.all()
    latest_productions_list     = Production.objects.all()
    latest_recipes_list         = Recipe.objects.all()

    readonly = True

    if request.method == "POST":
        if "delete" in request.POST:
            Product.objects.get(pk = product_id).delete()
        if "edit" in request.POST:
            readonly = False
        if "save" in request.POST:
            obj = Product.objects.get(pk = product_id)
            obj.product_name = request.POST.get('product_name')
            obj.save()
    
    if Product.objects.filter(pk=product_id).exists():
        product = Product.objects.get(pk = product_id)
    else:
        product = False
    
    context = {
        "latest_deliveries_list": latest_deliveries_list,
        "latest_products_list": latest_products_list,
        "latest_compositions_list": latest_compositions_list,
        "latest_productions_list": latest_productions_list,
        "latest_recipes_list": latest_recipes_list,
        "product": product,
        "newly_created" : False,
        "readonly" : readonly,
    }
    return render(request, "warehouse/product.html", context)

def new_delivery(request):
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
    return render(request, "warehouse/add_delivery.html", context)

def delivery(request, delivery_id):
    latest_deliveries_list      = Delivery.objects.all()
    latest_products_list        = Product.objects.all()
    latest_compositions_list    = Composition.objects.all()
    latest_productions_list     = Production.objects.all()
    latest_recipes_list         = Recipe.objects.all()
    delivery = Delivery.objects.get(pk = delivery_id)

    context = {
        "latest_deliveries_list": latest_deliveries_list,
        "latest_products_list": latest_products_list,
        "latest_compositions_list": latest_compositions_list,
        "latest_productions_list": latest_productions_list,
        "latest_recipes_list": latest_recipes_list,
        "delivery": delivery,
    }

    return render(request, "warehouse/delivery.html", context)

def new_recipe(request):
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
    return render(request, "warehouse/add_recipe.html", context)

def recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk = recipe_id)
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
        "recipe": recipe,
    }
    return render(request, "warehouse/recipe.html", context)

def new_composition(request):
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
    return render(request, "warehouse/add_composition.html", context)

def composition(request, composition_id):
    composition = Composition.objects.get(pk = composition_id)
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
        "composition": composition,
    }
    return render(request, "warehouse/composition.html", context)

def new_production(request):
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
    return render(request, "warehouse/add_production.html", context)

def production(request, production_id):
    production = Production.objects.get(pk = production_id)
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