from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create$', views.CreateTicket.as_view(), name='create'),
    url(r'^$', views.GetTicket.as_view(), name='get_user_tickets'),
    url(r'^use$', views.UseTicket.as_view(), name='use')
]
