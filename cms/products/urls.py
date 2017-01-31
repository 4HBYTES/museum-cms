from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_all, name='get_all'),
    url(r'^(?P<product_id>[0-9a-z\-]+)$', views.get_one, name='get_one'),
]
