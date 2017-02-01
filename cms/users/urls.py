from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^signin$', views.SigninView.as_view(), name='signin'),
    url(r'^signup$', views.SignupView.as_view(), name='signup'),
    url(r'^password$', views.PasswordView.as_view(), name='change_password'),
    url(r'^profile$', views.ProfileView.as_view(), name='profile'),
]
