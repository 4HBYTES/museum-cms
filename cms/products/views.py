from django.http import HttpResponse
from django.views.generic import View
from .models import Product
import json


class ProductsView(View):

    def get(self, request):
        all_products = []
        products = Product.objects.all()
        for product in products:
            all_products.append(product.to_view())

        json_products = json.dumps(all_products)
        return HttpResponse(json_products, content_type='application/json')


class ProductView(View):

    def get(self, request, product_id):
        product = None
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            json_error = json.dumps({'error': 'does not exists'})
            return HttpResponse(
                json_error,
                status=404,
                content_type='application/json'
            )

        json_product = json.dumps(product.to_view())
        return HttpResponse(json_product, content_type='application/json')
