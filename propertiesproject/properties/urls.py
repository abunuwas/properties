from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='property_index'),
    path('post/', views.property_create, name='property_create'),
]