from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_product/", views.new_product, name="dodawanie produktu"),
    path("add_delivery/", views.new_delivery, name="dodawanie dostawy"),
    path("add_composition/", views.new_composition, name="dodawanie składu"),
    path("add_recipe/", views.new_recipe, name="dodawanie receptury"),
    path("add_production/", views.new_production, name="dodawanie produkcji"),
    path("stan_magaznowy/", views.stan_magazynowy, name="stan magazynowy"),
    path("archiwum_produkcji/", views.archiwum_produkcji, name="archiwum produkcji"),
    path("archiwum_dostaw/", views.archiwum_dostaw, name="archiwum dostaw"),
    path("archiwum_dostaw/<int:product_id>/", views.archiwum_dostaw_p, name="archiwum dostaw produktu"),
    path("calculate_recipe/<int:composition_id>/", views.calculate_recipe, name="oblicz recepture"),
    path("calculate_production/<int:recipe_id>/", views.calculate_production, name="ułóż produkcje"),
]