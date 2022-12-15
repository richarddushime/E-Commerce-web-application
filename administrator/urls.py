from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('error/', views.error, name='error'),
    path('blank/', views.blank, name='blank'),
    path('button/', views.button, name='button'),
    path('chart/', views.chart, name='chart'),
    path('element/', views.element, name='element'),
    path('form/', views.form, name='form'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('table/', views.table, name='table'),
    path('typography/', views.typography, name='typography'),
    path('widget/', views.widget, name='widget'),
    

]