from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^signin$', views.signin, name='signin'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^password$', views.change_password, name='change_password'),
    url(r'^profile$', views.profile, name='profile'),
]
