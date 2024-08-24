from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("delivery/<int:delivery_id>/", views.delivery, name="widok dostawy"),
    path("product/<int:product_id>/", views.product, name="widok produktu"),
    path("composition/<int:composition_id>/", views.composition, name="widok składu"),
    path("recipe/<int:recipe_id>/", views.recipe, name="widok receptury"),
    path("production/<int:production_id>/", views.production, name="widok zlecenia produkcji"),

    path("add_product/", views.new_product, name="dodawanie produktu"),
    path("add_delivery/", views.new_delivery, name="dodawanie dostawy"),
    path("add_composition/", views.new_composition, name="dodawanie składu"),
    path("add_recipe/", views.new_recipe, name="dodawanie receptury"),
    path("add_production/", views.new_production, name="dodawanie produkcji"),

    path("instruction/", views.instruction, name="instrukcja użytkowania systemu"),

    path("stan_magazynowy/", views.stan_magazynowy, name="stan magazynowy"),

    path("lista_produkcji/", views.lista_produkcji, name="lista produkcji"),

    path("archiwum_dostaw/", views.archiwum_dostaw, name="archiwum dostaw"),
    
    path("calculate_recipe/", views.calculate_recipe, name="oblicz recepture"),
]