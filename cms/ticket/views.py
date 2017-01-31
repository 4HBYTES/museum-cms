from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Ticket
from users.models import FrontUser
from products.models import Product
import json
from datetime import datetime


@csrf_exempt
def create(request):
    '''
    Create ticket(s)
    '''
    data = json.loads(request.body)

    token = data['token']
    app_token = getattr(settings, 'APP_TOKEN', None)

    if token != app_token:
        json_data = json.dumps({'error': 'invalid token'})
        return HttpResponse(
            json_data,
            status=400,
            content_type='application/json'
        )

    quantity = int(data['quantity'])
    product_id = data['product_id']
    user_id = data['user_id']

    for i in range(quantity):
        # TODO: This is where we can do: QR code, email sending, etc
        ticket = Ticket(
            created_at=datetime.now(),
            product=Product.objects.get(id=product_id),
            user=FrontUser.objects.get(id=user_id),
            used=False
        )
        ticket.save()

    return HttpResponse({}, status=201, content_type='application/json')


@csrf_exempt
def use(request):
    '''
    Use a ticket
    '''
    data = json.loads(request.body)

    token = data['token']
    app_token = getattr(settings, 'APP_TOKEN', None)

    if token != app_token:
        json_data = json.dumps({'error': 'invalid token'})
        return HttpResponse(
            json_data,
            status=400,
            content_type='application/json'
        )

    ticket_id = data['ticket_id']

    ticket = None
    try:
        ticket = Ticket.objects.get(id=ticket_id)
    except Ticket.DoesNotExist:
        return HttpResponse({}, status=404, content_type='application/json')

    if ticket.used:
        return HttpResponse({}, status=409, content_type='application/json')

    ticket.used = True
    ticket.save()

    return HttpResponse({}, status=200, content_type='application/json')
