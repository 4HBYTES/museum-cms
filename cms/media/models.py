from __future__ import unicode_literals

from django.db import models

import uuid


def make_uuid():
    return uuid.uuid4()


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=make_uuid)
    name = models.CharField(max_length=30)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''
        This is used by the 'Recent actions' widget in the admin.
        '''
        return '{}'.format(self.name)

    def to_view(self):
        return {
            'name': self.name,
            'description': self.description,
            'id': str(self.id),
            'created_at': self.created_at.isoformat()
        }


class Event(models.Model):
    # TODO: This probably should be a separate model
    MUSEUM_CHOICES = (
        ('PH', 'Perfume House'),
        ('SC', 'Story of the Creek')
    )

    id = models.UUIDField(primary_key=True, default=make_uuid)
    name = models.CharField(max_length=30)
    description = models.TextField()
    place = models.CharField(
        choices=MUSEUM_CHOICES,
        default='PH',
        max_length=100
    )
    date = models.DateTimeField()

    def __str__(self):
        '''
        This is used by the 'Recent actions' widget in the admin.
        '''
        return '{}'.format(self.name)

    def to_view(self):
        return {
            'name': self.name,
            'description': self.description,
            'id': str(self.id),
            'place': self.place,
            'date': self.date.isoformat()
        }
