from django.urls import path
from .views import home, register

urlpatterns = [
  path('', home, name='home'),
  path('', register, name='register')
]