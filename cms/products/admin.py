from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'currency', )

    list_display = ('name', 'price', 'currency',)

    search_fields = ['name']


admin.site.register(Product, ProductAdmin)
