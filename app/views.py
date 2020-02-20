from django.shortcuts import render, redirect
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm, UploadForm
from django.contrib.auth.models import User
from api.models import Projects
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
  projects = Projects.objects.all()
  return render(request, 'home.html', {'projects':projects})

def register(request):
    if request.method == "POST":
      register=RegisterForm(request.POST)
      if register.is_valid():
        register.save()
        username = register.cleaned_data.get("username")
        messages.success(request, ("Account for {} has been created successfully").format(username))
        return redirect("signin")
    else:
      register=RegisterForm()
  
    return render(request, 'users/signup.html', {'register':register})

@login_required()
def profile(request):

  return render(request, "users/profile.html")


@login_required()
def edit_profile(request):
  if request.method == "POST":
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save()
      messages.success(request, "Profile updated successfully")
      return redirect("edit_profile")

  else:
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user)
  context = {
    "u_form" : u_form,
    "p_form" : p_form
  }
  return render(request, "users/edit_profile.html", context)
  
@login_required()
def upload(request):
 
  if request.method == "POST":
    upload_form = UploadForm(request.POST, request.FILES)
    if upload_form.is_valid():
      upload_form.save()
      return redirect("home")
  else:
    upload_form = UploadForm()
    
  
  return render(request, "users/upload.html", {"upload_form":upload_form})
