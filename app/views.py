from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.

def home(request):
  return render(request, 'home.html')

def register(request):
  register = RegisterForm()
  return render(request, 'users/signup.html', {'register':register})
