from django.urls import path
from .views import home, register
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('', home, name='home'),
  path('signin/', auth_views.LoginView.as_view(template_name='users/signin.html'), name='signin'),
  path('signout/', auth_views.LogoutView.as_view(template_name='home.html'), name='signout'),
  path('register/', register, name='register')
]