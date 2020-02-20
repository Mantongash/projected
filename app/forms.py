from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile
from api.models import Projects

class RegisterForm(UserCreationForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ["username", "email"]

class ProfileUpdateForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ["image"]


class UploadForm(forms.ModelForm):
  class Meta:
    model = Projects
    fields = ['title',"image", "description", 'link']