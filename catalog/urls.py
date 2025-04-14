from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='catalog-home'),
    path('contacts/', views.contacts, name='catalog-contacts')
]