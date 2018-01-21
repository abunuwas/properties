from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.property_add, name='property_add'),
]