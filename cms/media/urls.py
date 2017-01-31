from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^news$', views.get_news, name='get_news'),
    url(r'^events$', views.get_events, name='get_events'),
]
