from django.http import HttpResponse
from django.views.generic import View
from django.conf import settings
from .models import Ticket
from users.models import FrontUser
from users.utils import basicauth
from products.models import Product
import json
from datetime import datetime


class CreateTicket(View):

    def post(self, request):
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

        user_id = data['user_id']
        for item in data['products']:
            quantity = int(item['quantity'])
            product_id = item['product_id']

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


class UseTicket(View):

    def post(self, request):
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


class GetTicket(View):

    @basicauth
    def get(self, request):
        user_id = request.user.id

        all_tickets = []
        tickets = Ticket.objects.filter(user__id=user_id).filter(used=False)
        for ticket in tickets:
            all_tickets.append(ticket.to_view())

        json_tickets = json.dumps(all_tickets)
        return HttpResponse(json_tickets, content_type='application/json')
