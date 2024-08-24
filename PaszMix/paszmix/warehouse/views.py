from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from warehouse.create_recipe import *

from .models import Delivery, Product, Composition, Production, Recipe, RecipeElement, ProductionElement

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
            obj.wilgotnosc = request.POST.get('wilgotnosc')
            obj.energia_metaboliczna = request.POST.get('energia_metaboliczna')
            obj.bialko_ogolne = request.POST.get('bialko_ogolne')
            obj.lizyna = request.POST.get('lizyna')
            obj.metionina = request.POST.get('metionina')
            obj.cystyna = request.POST.get('cystyna')
            obj.treonina = request.POST.get('treonina')
            obj.tryptofan = request.POST.get('tryptofan')
            obj.arginina = request.POST.get('arginina')
            obj.walina = request.POST.get('walina')
            obj.izoleucyna = request.POST.get('izoleucyna')
            obj.wapn = request.POST.get('wapn')
            obj.fosfor_przyswajalny = request.POST.get('fosfor_przyswajalny')
            obj.sod = request.POST.get('sod')
            obj.kwas_linolowy = request.POST.get('kwas_linolowy')
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

    if request.method == "POST":
        product = Product.objects.get(pk = request.POST.get('product'))
        price = request.POST.get('price')
        date = request.POST.get('date')
        initial_quantity = request.POST.get('initial_quantity')
        used_quantity = request.POST.get('used_quantity')
        waste = request.POST.get('waste')
        is_finished = request.POST.get('is_finished')
        
        if product:
            Delivery.objects.create(product = product, 
                                   price = price, 
                                   date = date, 
                                   initial_quantity = initial_quantity, 
                                   used_quantity = used_quantity,
                                   waste = waste, 
                                   is_finished = (is_finished=="True"))
            delivery = Delivery.objects.last()
            
            context = {
                "latest_deliveries_list": latest_deliveries_list,
                "latest_products_list": latest_products_list,
                "latest_compositions_list": latest_compositions_list,
                "latest_productions_list": latest_productions_list,
                "latest_recipes_list": latest_recipes_list,
                "delivery": delivery,
                "newly_created" : True,
                "readonly" : True
             }
            return render(request, "warehouse/delivery.html", context)

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

    readonly = True

    if request.method == "POST":
        if "delete" in request.POST:
            Delivery.objects.get(pk = delivery_id).delete()
        if "edit" in request.POST:
            readonly = False
        if "save" in request.POST:
            obj = Delivery.objects.get(pk = delivery_id)
            obj.product = Product.objects.get(pk = request.POST.get('product'))
            obj.price = request.POST.get('price')
            obj.date = request.POST.get('date')
            obj.initial_quantity = request.POST.get('initial_quantity')
            obj.used_quantity = request.POST.get('used_quantity')
            obj.waste = request.POST.get('waste')
            obj.is_finished = (request.POST.get('is_finished')=="True")
            obj.save()

    if Delivery.objects.filter(pk=delivery_id).exists():
        delivery = Delivery.objects.get(pk = delivery_id)
    else:
        delivery = False
    
    context = {
        "latest_deliveries_list": latest_deliveries_list,
        "latest_products_list": latest_products_list,
        "latest_compositions_list": latest_compositions_list,
        "latest_productions_list": latest_productions_list,
        "latest_recipes_list": latest_recipes_list,
        "delivery": delivery,
        "newly_created" : False,
        "readonly" : readonly,
    }

    return render(request, "warehouse/delivery.html", context)

def new_recipe(request):
    latest_deliveries_list      = Delivery.objects.all()
    latest_products_list        = Product.objects.all()
    latest_compositions_list    = Composition.objects.all()
    latest_productions_list     = Production.objects.all()
    latest_recipes_list         = Recipe.objects.all()

    if request.method == "POST":
        if "create_recipe" in request.POST:
            name = request.POST.get('name')
            type = request.POST.get('type')
            number_of_positions = int(request.POST.get('number_of_positions'))

            if name != "":
                Recipe.objects.create( composition = Composition.objects.get(pk = request.POST.get('composition')), 
                                    name = name,
                                    type = type,
                                    number_of_positions = number_of_positions)
                recipe = Recipe.objects.last()
                
                context = {
                    "latest_deliveries_list": latest_deliveries_list,
                    "latest_products_list": latest_products_list,
                    "latest_compositions_list": latest_compositions_list,
                    "latest_productions_list": latest_productions_list,
                    "latest_recipes_list": latest_recipes_list,
                    "recipe": recipe,
                    "number_of_positions": range(number_of_positions),
                }
                return render(request, "warehouse/add_recipe.html", context)
            
        if "add_recipe_elements" in request.POST:
            recipe = Recipe.objects.last()

            for i in range(recipe.number_of_positions):
                print("dodajemy recipe elem")
                pname = 'product'+str(i)
                print(pname)
                p = request.POST.get(pname)
                print(p)
                prod = Product.objects.get(pk = p)
                print(prod)
                quan = float(request.POST.get('quantity'+str(i)))
                print(quan)
                RecipeElement.objects.create(recipe_ref = recipe, product = prod, quantity = quan)

            recipe_elems = RecipeElement.objects.filter(recipe_ref = recipe.pk)

            context = {
            "latest_deliveries_list": latest_deliveries_list,
            "latest_products_list": latest_products_list,
            "latest_compositions_list": latest_compositions_list,
            "latest_productions_list": latest_productions_list,
            "latest_recipes_list": latest_recipes_list,
            "recipe": recipe,
            "recipe_elems": recipe_elems,
            "newly_created" : True,
            "readonly" : True,
            "how_many_empty" : False,
            }

            return render(request, "warehouse/recipe.html", context)

    context = {
        "latest_deliveries_list": latest_deliveries_list,
        "latest_products_list": latest_products_list,
        "latest_compositions_list": latest_compositions_list,
        "latest_productions_list": latest_productions_list,
        "latest_recipes_list": latest_recipes_list,
        "number_of_positions": -1,
        "recipe": False,
    }
    return render(request, "warehouse/add_recipe.html", context)

def recipe(request, recipe_id):
    latest_deliveries_list      = Delivery.objects.all()
    latest_products_list        = Product.objects.all()
    latest_compositions_list    = Composition.objects.all()
    latest_productions_list     = Production.objects.all()
    latest_recipes_list         = Recipe.objects.all()

    readonly = True

    if request.method == "POST":
        if "edit" in request.POST:
            readonly = False
        obj = Recipe.objects.get(pk = recipe_id)
        recipe_elems = RecipeElement.objects.filter(recipe_ref = obj)
        for i in range(obj.number_of_positions):
            del_nam = "delete"+str(i)
            if del_nam in request.POST:
                recipe_elems[i].delete()

        if "delete" in request.POST:
            Recipe.objects.get(pk = recipe_id).delete()
        if "save" in request.POST:
            obj.composition = Composition.objects.get(pk=request.POST.get('composition'))
            old_number_of_positions = obj.number_of_positions
            obj.number_of_positions = int(request.POST.get('number_of_positions'))
            obj.name = request.POST.get('name')
            obj.type = request.POST.get('type')
            obj.save()

            recipe_elems = RecipeElement.objects.filter(recipe_ref = obj)

            for i,j in enumerate(recipe_elems):
                pname = 'product'+str(i)
                j.product = Product.objects.get(pk=request.POST.get(pname))
                j.quantity = float(request.POST.get('quantity'+str(i)))
                if j.quantity > 0:
                    j.save()
                else: j.delete()

            for i in range(recipe_elems.count(), old_number_of_positions):
                pname = 'product'+str(i)
                product = Product.objects.get(pk=request.POST.get(pname))
                quantity = float(request.POST.get('quantity'+str(i)))
                if quantity > 0:
                    RecipeElement.objects.create(recipe_ref = obj, product = product, quantity = quantity)
    
    if Recipe.objects.filter(pk=recipe_id).exists():
        recipe = Recipe.objects.get(pk = recipe_id)
        recipe_elems = RecipeElement.objects.filter(recipe_ref = recipe)    
        how_many_empty = range(recipe_elems.count(), recipe.number_of_positions)
    else:
        recipe = False
        recipe_elems = False
        how_many_empty = False
        
    context = {
        "latest_deliveries_list": latest_deliveries_list,
        "latest_products_list": latest_products_list,
        "latest_compositions_list": latest_compositions_list,
        "latest_productions_list": latest_productions_list,
        "latest_recipes_list": latest_recipes_list,
        "recipe": recipe,
        "recipe_elems": recipe_elems,
        "newly_created" : False,
        "readonly" : readonly,
        "how_many_empty" : how_many_empty,
    }

    return render(request, "warehouse/recipe.html", context)

def new_composition(request):
    latest_deliveries_list      = Delivery.objects.all()
    latest_products_list        = Product.objects.all()
    latest_compositions_list    = Composition.objects.all()
    latest_productions_list     = Production.objects.all()
    latest_recipes_list         = Recipe.objects.all()

    if request.method == "POST":
        composition_name = request.POST.get('composition_name')
        energia_metaboliczna_min = request.POST.get('energia_metaboliczna_min')
        energia_metaboliczna_max = request.POST.get('energia_metaboliczna_max')
        lizyna = request.POST.get('lizyna')
        metionina = request.POST.get('metionina')
        cystyna_metionina = request.POST.get('cystyna_metionina')
        treonina = request.POST.get('treonina')
        tryptofan = request.POST.get('tryptofan')
        arginina = request.POST.get('arginina')
        walina = request.POST.get('walina')
        izoleucyna = request.POST.get('izoleucyna')
        wapn = request.POST.get('wapn')
        fosfor_przyswajalny = request.POST.get('fosfor_przyswajalny')
        sod = request.POST.get('sod')

        if composition_name != "":
            Composition.objects.create(composition_name = composition_name, 
                                   energia_metaboliczna_min = energia_metaboliczna_min,
                                   energia_metaboliczna_max = energia_metaboliczna_max, 
                                   lizyna = lizyna,
                                   metionina = metionina, 
                                   cystyna_metionina = cystyna_metionina, 
                                   treonina = treonina, 
                                   tryptofan = tryptofan, 
                                   arginina = arginina, 
                                   walina = walina, 
                                   izoleucyna = izoleucyna, 
                                   wapn = wapn, 
                                   fosfor_przyswajalny = fosfor_przyswajalny, 
                                   sod = sod)
            composition = Composition.objects.last()

            context = {
                "latest_deliveries_list": latest_deliveries_list,
                "latest_products_list": latest_products_list,
                "latest_compositions_list": latest_compositions_list,
                "latest_productions_list": latest_productions_list,
                "latest_recipes_list": latest_recipes_list,
                "composition": composition,
                "newly_created" : True,
                "readonly" : True
             }
            return render(request, "warehouse/composition.html", context)

    context = {
        "latest_deliveries_list": latest_deliveries_list,
        "latest_products_list": latest_products_list,
        "latest_compositions_list": latest_compositions_list,
        "latest_productions_list": latest_productions_list,
        "latest_recipes_list": latest_recipes_list,
    }
    return render(request, "warehouse/add_composition.html", context)

def composition(request, composition_id):
    latest_deliveries_list      = Delivery.objects.all()
    latest_products_list        = Product.objects.all()
    latest_compositions_list    = Composition.objects.all()
    latest_productions_list     = Production.objects.all()
    latest_recipes_list         = Recipe.objects.all()

    readonly = True

    if request.method == "POST":
        if "delete" in request.POST:
            Composition.objects.get(pk = composition_id).delete()
        if "edit" in request.POST:
            readonly = False
        if "save" in request.POST:
            obj = Composition.objects.get(pk = composition_id)
            obj.composition_name = request.POST.get('composition_name')
            obj.energia_metaboliczna_min = request.POST.get('energia_metaboliczna_min')
            obj.energia_metaboliczna_max = request.POST.get('energia_metaboliczna_max')
            obj.lizyna = request.POST.get('lizyna')
            obj.metionina = request.POST.get('metionina')
            obj.cystyna_metionina = request.POST.get('cystyna_metionina')
            obj.treonina = request.POST.get('treonina')
            obj.tryptofan = request.POST.get('tryptofan')
            obj.arginina = request.POST.get('arginina')
            obj.walina = request.POST.get('walina')
            obj.izoleucyna = request.POST.get('izoleucyna')
            obj.wapn = request.POST.get('wapn')
            obj.fosfor_przyswajalny = request.POST.get('fosfor_przyswajalny')
            obj.sod = request.POST.get('sod')
            obj.save()
    
    if Composition.objects.filter(pk=composition_id).exists():
        composition = Composition.objects.get(pk = composition_id)
    else:
        composition = False
    
    context = {
        "latest_deliveries_list": latest_deliveries_list,
        "latest_products_list": latest_products_list,
        "latest_compositions_list": latest_compositions_list,
        "latest_productions_list": latest_productions_list,
        "latest_recipes_list": latest_recipes_list,
        "composition": composition,
        "newly_created" : False,
        "readonly" : readonly,
    }
    return render(request, "warehouse/composition.html", context)

def new_production(request):
    latest_deliveries_list      = Delivery.objects.all()
    latest_products_list        = Product.objects.all()
    latest_compositions_list    = Composition.objects.all()
    latest_productions_list     = Production.objects.all()
    latest_recipes_list         = Recipe.objects.all()

    if request.method == "POST":
        if "create_production" in request.POST:
            recipe = Recipe.objects.get(pk = request.POST.get('recipe'))
            date = request.POST.get('date')
            name_of_final_product = request.POST.get('name_of_final_product')
            Production.objects.create(recipe = recipe, date = date, name_of_final_product = name_of_final_product)
            production = Production.objects.last()
            recipe_elems = RecipeElement.objects.filter(recipe_ref = recipe.pk).filter(quantity__gt=0)

            context = {
                "latest_deliveries_list": latest_deliveries_list,
                "latest_products_list": latest_products_list,
                "latest_compositions_list": latest_compositions_list,
                "latest_productions_list": latest_productions_list,
                "latest_recipes_list": latest_recipes_list,
                "production" : production,
                "recipe_elems" : enumerate(recipe_elems),
            }
            return render(request, "warehouse/add_production.html", context)
        
        if "add_productions_elements" in request.POST:
            production = Production.objects.last()
            recipe_elems = RecipeElement.objects.filter(recipe_ref = production.recipe.pk).filter(quantity__gt=0)
            for i in range(recipe_elems.count()):
                delivery_name = "delivery"+str(i)
                quantity_name = "quantity"+str(i)

                if Delivery.objects.filter(pk=request.POST.get(delivery_name)).exists():
                    delivery = Delivery.objects.get(pk = request.POST.get(delivery_name))
                    quantity = float(request.POST.get(quantity_name))
                    if quantity > 0:
                        ProductionElement.objects.create(production_ref = production, delivery_ref = delivery, quantity=quantity)

                delivery_name = "2delivery"+str(i)
                quantity_name = "2quantity"+str(i)

                if Delivery.objects.filter(pk=request.POST.get(delivery_name)).exists():
                    delivery = Delivery.objects.get(pk = request.POST.get(delivery_name))
                    quantity = float(request.POST.get(quantity_name))
                    if quantity > 0:
                        ProductionElement.objects.create(production_ref = production, delivery_ref = delivery, quantity=quantity)

                delivery_name = "3delivery"+str(i)
                quantity_name = "3quantity"+str(i)
                if Delivery.objects.filter(pk=request.POST.get(delivery_name)).exists():
                    delivery = Delivery.objects.get(pk = request.POST.get(delivery_name))
                    quantity = float(request.POST.get(quantity_name))
                    if quantity > 0:
                        ProductionElement.objects.create(production_ref = production, delivery_ref = delivery, quantity=quantity)

            production_elements = ProductionElement.objects.filter(production_ref = production.pk)

            context = {
                "latest_deliveries_list": latest_deliveries_list,
                "latest_products_list": latest_products_list,
                "latest_compositions_list": latest_compositions_list,
                "latest_productions_list": latest_productions_list,
                "latest_recipes_list": latest_recipes_list,
                "newly_created" : True,
                "production" : production,
                "production_elements" : production_elements,
            }

            return render(request, "warehouse/production.html", context)

    context = {
        "latest_deliveries_list": latest_deliveries_list,
        "latest_products_list": latest_products_list,
        "latest_compositions_list": latest_compositions_list,
        "latest_productions_list": latest_productions_list,
        "latest_recipes_list": latest_recipes_list,
        "production" : False
    }
    return render(request, "warehouse/add_production.html", context)

def production(request, production_id):
    latest_deliveries_list      = Delivery.objects.all()
    latest_products_list        = Product.objects.all()
    latest_compositions_list    = Composition.objects.all()
    latest_productions_list     = Production.objects.all()
    latest_recipes_list         = Recipe.objects.all()

    if request.method == "POST":
        if "delete" in request.POST:
            Production.objects.get(pk = production_id).delete()

    if Production.objects.filter(pk=production_id).exists():
        production = Production.objects.get(pk = production_id)
        production_elements = ProductionElement.objects.filter(production_ref = production.pk)
    else:
        production = False
        production_elements = False

    context = {
        "latest_deliveries_list": latest_deliveries_list,
        "latest_products_list": latest_products_list,
        "latest_compositions_list": latest_compositions_list,
        "latest_productions_list": latest_productions_list,
        "latest_recipes_list": latest_recipes_list,
        "newly_created" : False,
        "production": production,
        "production_elements" : production_elements,
    }
    return render(request, "warehouse/production.html", context)

def stan_magazynowy(request):
    latest_deliveries_list      = Delivery.objects.all()
    latest_products_list        = Product.objects.all()
    latest_compositions_list    = Composition.objects.all()
    latest_productions_list     = Production.objects.all()
    latest_recipes_list         = Recipe.objects.all()

    class del_prod():
        def __init__(self, product, quantity, desc):
            self.product = product
            self.quantity = quantity
            self.desc = desc

    dict = []

    for delivery in Delivery.objects.filter(is_finished = False):
        poz_il = delivery.initial_quantity - delivery.used_quantity - delivery.waste
        filtered = filter(lambda x: x.product==delivery.product, dict)
        
        try:
            obj = filtered.__next__()
            obj.quantity += poz_il
            obj.desc.append((delivery, poz_il))
        except StopIteration:
            dict.append(del_prod(product = delivery.product, quantity=poz_il, desc=[(delivery, poz_il)]))

    context = {
        "latest_deliveries_list": latest_deliveries_list,
        "latest_products_list": latest_products_list,
        "latest_compositions_list": latest_compositions_list,
        "latest_productions_list": latest_productions_list,
        "latest_recipes_list": latest_recipes_list,
        "dict" : dict,
    }

    return render(request, "warehouse/stan_magazynowy.html", context)

def lista_produkcji(request):
    latest_deliveries_list      = Delivery.objects.all()
    latest_products_list        = Product.objects.all()
    latest_compositions_list    = Composition.objects.all()
    latest_productions_list     = Production.objects.all()
    latest_recipes_list         = Recipe.objects.all()

    class prod():
        def __init__(self, production, elems):
            self.production = production
            self.elems = elems

    productions = Production.objects.all().order_by('date')

    dict = []
    for p in productions:
        elems = []
        for e in ProductionElement.objects.filter(production_ref = p.pk):
            elems.append(e)
        dict.append(prod(p, elems))

    context = {
        "latest_deliveries_list": latest_deliveries_list,
        "latest_products_list": latest_products_list,
        "latest_compositions_list": latest_compositions_list,
        "latest_productions_list": latest_productions_list,
        "latest_recipes_list": latest_recipes_list,
        "dict" : dict,
    }
    return render(request, "warehouse/lista_produkcji.html", context)

def archiwum_dostaw(request):
    latest_deliveries_list      = Delivery.objects.all()
    latest_products_list        = Product.objects.all()
    latest_compositions_list    = Composition.objects.all()
    latest_productions_list     = Production.objects.all()
    latest_recipes_list         = Recipe.objects.all()

    arch_deliveries = []
    for i in Delivery.objects.filter(is_finished = True):
        arch_deliveries.append(i)

    context = {
        "latest_deliveries_list": latest_deliveries_list,
        "latest_products_list": latest_products_list,
        "latest_compositions_list": latest_compositions_list,
        "latest_productions_list": latest_productions_list,
        "latest_recipes_list": latest_recipes_list,
        "arch_deliveries" : arch_deliveries,
    }
    return render(request, "warehouse/archiwum_dostaw.html", context)

def calculate_recipe(request):
    latest_deliveries_list      = Delivery.objects.all()
    latest_products_list        = Product.objects.all()
    latest_compositions_list    = Composition.objects.all()
    latest_productions_list     = Production.objects.all()
    latest_recipes_list         = Recipe.objects.all()

    print("poczatke")

    if request.method == "POST" and  "create" in request.POST:
        print("dobra droga")
        sklad = Composition.objects.get(pk = request.POST.get('composition'))

        class pos():
            def __init__(self, product, dost_ilosc, srednia_cena):
                self.product = product
                self.dost_ilosc = dost_ilosc
                self.srednia_cena = srednia_cena

        list = []

        for p in latest_products_list:
            dels = Delivery.objects.filter(product = p.pk).filter(is_finished=False)
            p_il = 0.0
            p_cen = 0.0
            for d in dels:
                p_il += d.initial_quantity-d.used_quantity-d.waste
                p_cen += (float(d.price)/(d.initial_quantity-d.waste))* (d.initial_quantity-d.used_quantity-d.waste)
            if p_il > 0: list.append(pos(p, p_il, p_cen/p_il))

        recipe = False
        recipe_elems = False
        if create_recipe(sklad, list):
            recipe = Recipe.objects.last()
            recipe_elems = RecipeElement.objects.filter(recipe_ref = recipe.pk)

        context = {
            "latest_deliveries_list": latest_deliveries_list,
            "latest_products_list": latest_products_list,
            "latest_compositions_list": latest_compositions_list,
            "latest_productions_list": latest_productions_list,
            "latest_recipes_list": latest_recipes_list,
            "recipe": recipe,
            "recipe_elems": recipe_elems,
            "newly_created" : True,
            "readonly" : True,
            "how_many_empty" : False,
            "generated": True
            }

        return render(request, "warehouse/recipe.html", context)

    context = {
        "latest_deliveries_list": latest_deliveries_list,
        "latest_products_list": latest_products_list,
        "latest_compositions_list": latest_compositions_list,
        "latest_productions_list": latest_productions_list,
        "latest_recipes_list": latest_recipes_list,
    }
    return render(request, "warehouse/skomponuj_recepture.html", context)

def instruction(request):
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
    return render(request, "warehouse/instruction.html", context)