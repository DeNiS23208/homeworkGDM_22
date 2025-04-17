from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.home, name='catalog-home'),
    path('contacts/', views.contacts, name='catalog-contacts')
]
