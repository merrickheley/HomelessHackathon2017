from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.basic, name="basic"),
    url(r'^results', views.results, name="results"),
	url(r'^services', views.services, name='services'),
	url(r'^profile', views.profile, name='profile'),
	url(r'^about', views.about, name='about'),
	url(r'^contact', views.contact, name='contact'),
]