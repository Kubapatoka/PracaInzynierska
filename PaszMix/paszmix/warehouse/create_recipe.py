import math
import random
from .models import Recipe, RecipeElement, Composition

def ocena(composition, list_of_products, vec):
    s1000 = 1000

    energia_pasza = 0.0
    cena = 0.0
    lizyna = 0.0
    metionina = 0.0
    cystyna_metionina = 0.0
    treonina = 0.0
    tryptofan = 0.0
    arginina = 0.0
    walina = 0.0
    izoleucyna = 0.0
    wapn = 0.0
    fosfor_przyswajalny = 0.0
    sod = 0.0
    
    for i in range(len(vec)):
        energia_pasza += (list_of_products[i].product.energia_metaboliczna * vec[i])
        cena += (vec[i]*list_of_products[i].srednia_cena)
        lizyna += (vec[i]*list_of_products[i].product.lizyna/100)
        metionina += (vec[i]*list_of_products[i].product.metionina/100)
        cystyna_metionina += (vec[i]*list_of_products[i].product.cystyna/100 + vec[i]*list_of_products[i].product.metionina/100)
        treonina += (vec[i]*list_of_products[i].product.treonina/100)
        tryptofan += (vec[i]*list_of_products[i].product.tryptofan/100)
        arginina += (vec[i]*list_of_products[i].product.arginina/100)
        walina += (vec[i]*list_of_products[i].product.walina/100)
        izoleucyna += (vec[i]*list_of_products[i].product.izoleucyna/100)
        wapn += (vec[i]*list_of_products[i].product.wapn/100)
        fosfor_przyswajalny += (vec[i]*list_of_products[i].product.fosfor_przyswajalny/100)
        sod += (vec[i]*list_of_products[i].product.sod/100)

    print("cena:", cena)
    cz_en = 1

    if (s1000*composition.energia_metaboliczna_min) > energia_pasza: 
        diff = s1000*composition.energia_metaboliczna_min - energia_pasza
        wzgl = 100*(diff/(s1000*composition.energia_metaboliczna_min))
        if wzgl>1: cz_en = wzgl*1000
    if energia_pasza > s1000*composition.energia_metaboliczna_max: 
        diff = energia_pasza - s1000*composition.energia_metaboliczna_max
        wzgl = 100*(diff/(s1000*composition.energia_metaboliczna_max))
        if wzgl>1: cz_en = wzgl*1000
    
    # now energia paszy jest odpowiednio policzona
    if(cz_en > 1):
        print("ennnnnnnn", cz_en)
        energia_pasza = s1000*(composition.energia_metaboliczna_max+composition.energia_metaboliczna_min)/2

    czynnik = 1
    czynniki = []
    czynniki.append(1000*abs(composition.lizyna*energia_pasza/1000 - lizyna)/(composition.lizyna*energia_pasza/1000))
    czynniki.append(1000*abs(composition.metionina*energia_pasza/1000 - metionina)/(composition.metionina*energia_pasza/1000))
    czynniki.append(1000*abs(composition.cystyna_metionina*energia_pasza/1000 - cystyna_metionina)/(composition.cystyna_metionina*energia_pasza/1000))
    czynniki.append(1000*abs(composition.treonina*energia_pasza/1000 - treonina)/(composition.treonina*energia_pasza/1000))
    czynniki.append(1000*abs(composition.tryptofan*energia_pasza/1000 - tryptofan)/(composition.tryptofan*energia_pasza/1000))
    czynniki.append(1000*abs(composition.arginina*energia_pasza/1000 - arginina)/(composition.arginina*energia_pasza/1000))
    czynniki.append(1000*abs(composition.walina*energia_pasza/1000 - walina)/(composition.walina*energia_pasza/1000))
    czynniki.append(1000*abs(composition.izoleucyna*energia_pasza/1000 - izoleucyna)/(composition.izoleucyna*energia_pasza/1000))
    czynniki.append(1000*abs(composition.wapn*energia_pasza/1000 - wapn)/(composition.wapn*energia_pasza/1000))
    czynniki.append(1000*abs(composition.fosfor_przyswajalny*energia_pasza/1000 - fosfor_przyswajalny)/(composition.fosfor_przyswajalny*energia_pasza/1000))
    czynniki.append(1000*abs(composition.sod*energia_pasza/1000 - sod)/(composition.sod*energia_pasza/1000))

    for c in czynniki:
        #if c > 1:
        print("czynnik", c)
        czynnik += c

    return cena*czynnik*cz_en

def neighbour(vec, list, composition):
    new_vec = vec.copy()

    step = random.randint(1,300)
    n = len(vec)
    minus = random.randint(0,n-1)
    plus = random.randint(0,n-1)

    while new_vec[minus] < step+10 or minus == plus or new_vec[plus] + step > list[plus].dost_ilosc:
        step = random.randint(1,300)
        minus = random.randint(0,n-1)
        plus = random.randint(0,n-1)

    new_vec[minus] -= step
    new_vec[plus] += step

    nowa_cena = ocena(composition=composition, list_of_products=list, vec=new_vec)
    if nowa_cena  > ocena(composition=composition, list_of_products=list, vec=vec): 
        return neighbour(vec, list, composition)

    return (new_vec, nowa_cena)

def five_neighbours(vec, list, composition):
    res = []
    for i in range(20):
        new_vec = neighbour(vec, list, composition)
        if new_vec in res:
            i-=1
        else: 
            res.append(new_vec)

    return res

def create_recipe(composition, list_of_products):
    n = len(list_of_products)

    vec = [0] * n

    sum1000 = 1000
    for _ in range(100):
        while True:
            idx = random.randint(0,n-1)
            if list_of_products[idx].dost_ilosc > vec[idx]+10:    
                vec[idx] += 10
                break

    stan = five_neighbours(vec, list_of_products, composition)

    for _ in range(500):
        nowe_stany = []
        for s in stan:
            ss = five_neighbours(s[0], list_of_products, composition)
            nowe_stany.extend(ss)

        nowe_stany.sort(key = lambda x: x[1])
        nowy_stan = nowe_stany[:3]

        print("Nowy stan ma czynnik: ", nowy_stan[0][1], " stary: ", stan[0][1], "różnica: ", stan[0][1] - nowy_stan[0][1])
        if stan[0][1] - nowy_stan[0][1] < 1000000:
            recipe(nowy_stan[0][0],  list_of_products, composition)
            return True
        stan = nowy_stan

    return False

def recipe(vec, list, composition):
    number_of_positions = 0
    print(vec)
    for c in vec:
        print(c)
        if c > 0:
            number_of_positions += 1
    Recipe.objects.create( composition = composition, 
                                    name = composition.composition_name + "generated",
                                    type = "",
                                    number_of_positions = number_of_positions)

    recipe = Recipe.objects.last()
    for i,c in enumerate(vec):
        if c > 0:
            RecipeElement.objects.create(recipe_ref = recipe, product = list[i].product, quantity = c)