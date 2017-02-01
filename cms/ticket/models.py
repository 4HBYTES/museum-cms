from __future__ import unicode_literals
from django.db import models
from products.models import Product
from users.models import FrontUser
import uuid


def make_uuid():
    return uuid.uuid4()


class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=make_uuid)
    created_at = models.DateTimeField(auto_now=True)
    used = models.BooleanField()
    product = models.ForeignKey(Product)
    user = models.ForeignKey(FrontUser)

    def __str__(self):
        '''
        This is used by the 'Recent actions' widget in the admin.
        '''
        return '{}'.format(self.id)

    def to_view(self):
        return {
            'id': str(self.id),
            'product': self.product.to_view(),
            'created_at': self.created_at.isoformat()
        }
