from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Projects
from django.contrib.auth.models import User
from .serializers import ProjectsSerializer, UsersSerializer

class ListTodo(generics.ListAPIView):
  queryset = Projects.objects.all()
  serializer_class = ProjectsSerializer

class DetailTodo(generics.RetrieveAPIView):
  queryset = Projects.objects.all()
  serializer_class = ProjectsSerializer


class ListTodo(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UsersSerializer