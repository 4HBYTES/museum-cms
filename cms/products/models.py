from __future__ import unicode_literals
from django.db import models
import uuid

def make_uuid():
    return uuid.uuid4()

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=make_uuid)
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.FloatField()
    currency = models.CharField(max_length=3, default='USD')

    def to_view(self):
        return {
            'name': self.name,
            'description': self.description,
            'id': str(self.id),
            'price': self.price,
            'currency': self.currency
        }
