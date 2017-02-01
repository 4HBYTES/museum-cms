from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^news$', views.NewsView.as_view(), name='get_news'),
    url(r'^events$', views.EventsView.as_view(), name='get_events'),
]
