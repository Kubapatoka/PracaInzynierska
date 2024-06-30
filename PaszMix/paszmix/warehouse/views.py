from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world")

def new_product(request):
    return HttpResponse("Tu będzie formularz do dodania nowego produktu")

def new_delivery(request):
    return HttpResponse("Tu będzie formularz do dodania nowej dostawy")

def new_recipe(request):
    return HttpResponse("Tu będzie formularz do dodania nowego przepisu")

def new_composition(request):
    return HttpResponse("tu będzie dodanie nowego składu")

def new_production(request):
    return HttpResponse("tu będzie dodanie zlecenia produkcji")

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