from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from . import views
from . import validation
urlpatterns = [
    url(r'^landing/', views.landing, name='landing')
]