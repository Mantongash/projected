from rest_framework import serializers
from .models import Projects
from django.contrib.auth.models import User

class ProjectsSerializer(serializers.ModelSerializer):
  class Meta:
  model = Projects
  fields = ('id', 'title', 'image','description','link')

class UsersSerializer(serializers.ModelSerializer):
  class Meta:
  model = User
  fields = ('id', 'username', 'email')