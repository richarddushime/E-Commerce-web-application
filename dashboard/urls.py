from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cart/', views.cart, name='cart'),
    path('chechout/', views.chechout, name='chechout'),
    path('contact/', views.contact, name='contact'),
    path('detail/', views.detail, name='detail'),
    path('shop/', views.shop, name='shop'),
    ]