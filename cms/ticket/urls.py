from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create$', views.create, name='create'),
    url(r'^$', views.get_user_tickets, name='get_user_tickets'),
    url(r'^use$', views.use, name='use')
]
