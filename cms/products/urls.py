from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ProductsView.as_view(), name='get_all'),
    url(r'^(?P<product_id>[0-9a-z\-]+)$', views.ProductView.as_view(), name='get_one'),
]
