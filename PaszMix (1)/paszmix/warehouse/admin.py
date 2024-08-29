from django.contrib import admin

from .models import Delivery, Product, Composition

admin.site.register(Delivery)
admin.site.register(Product)
admin.site.register(Composition)
