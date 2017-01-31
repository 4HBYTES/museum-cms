from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Product
import json
import uuid

def get_all(request):
    all_products = []
    products = Product.objects.all()
    for product in products:
        all_products.append(product.to_view())

    json_products = json.dumps(all_products)
    return HttpResponse(json_products, content_type='application/json')

def get_one(request, product_id):
    product = None
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponse({'error': 'does not exists'}, status=404, content_type='application/json')

    json_product = json.dumps(product.to_view())
    return HttpResponse(json_product, content_type='application/json')
