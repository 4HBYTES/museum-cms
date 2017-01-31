from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'currency', )

    list_display = ('name', 'price', 'currency',)

admin.site.register(Product, ProductAdmin)
