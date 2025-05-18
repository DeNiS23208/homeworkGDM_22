from django.urls import path

from catalog.urls import urlpatterns
from .views import RegisterView

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),

]
