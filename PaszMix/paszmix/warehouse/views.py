from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from .models import Delivery, Product, Composition, Production, Recipe, RecipeElement

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

    print("aa\n")
    print(delivery.date)
    print("aa\n")

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
        if "delete" in request.POST:
            Recipe.objects.get(pk = recipe_id).delete()
        if "edit" in request.POST:
            readonly = False
        obj = Recipe.objects.get(pk = recipe_id)
        recipe_elems = RecipeElement.objects.filter(recipe_ref = obj)
        for i in range(obj.number_of_positions):
            del_nam = "delete"+str(i)
            if del_nam in request.POST:
                print("usuwansko")
                recipe_elems[i].delete()

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
                j.save()

            for i in range(recipe_elems.count(), old_number_of_positions):
                pname = 'product'+str(i)
                product = Product.objects.get(pk=request.POST.get(pname))
                quantity = float(request.POST.get('quantity'+str(i)))
                RecipeElement.objects.create(recipe_ref = obj, product = product, quantity = quantity)
    
    if Recipe.objects.filter(pk=recipe_id).exists():
        recipe = Recipe.objects.get(pk = recipe_id)
        recipe_elems = RecipeElement.objects.filter(recipe_ref = recipe)    
        how_many_empty = range(recipe_elems.count(), recipe.number_of_positions)

    else:
        recipe = False
        recipe_elems = False
        how_many_empty = False
    
    print("how many empty:")
    print(how_many_empty)
    if how_many_empty:
        for i in how_many_empty:
            print(i)
        print("end")

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
    composition = Composition.objects.get(pk = composition_id)
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