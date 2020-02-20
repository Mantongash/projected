from django.urls import path
from .views import ListProjects, DetailProjects, ListUsers

urlpatterns = [
  path('<int:pk>/', DetailProjects.as_view()),
  path('projects/', ListProjects.as_view()),
  path('users/', ListUsers.as_view()),
  ]