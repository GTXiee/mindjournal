from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth import views as auth_views
from . import views
from django.views.generic.base import TemplateView
from .forms import CustomAuthenticationForm

urlpatterns = [
    # url(r'^$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', auth_views.LoginView.as_view(authentication_form=CustomAuthenticationForm), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^thanks/$', views.thanks, name='thanks'),
]
