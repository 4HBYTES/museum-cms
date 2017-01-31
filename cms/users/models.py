from __future__ import unicode_literals
import uuid

from django.db import models

def make_uuid():
    return uuid.uuid4()

class FrontUser(models.Model):
    id = models.UUIDField(primary_key=True, default=make_uuid)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        '''
        This is used by the 'Recent actions' widget in the admin.
        '''
        return '[User] {} {}'.format(self.first_name, self.last_name)

    def to_view(self):
        return {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name
        }
