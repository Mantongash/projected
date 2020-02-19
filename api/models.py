from django.db import models

# Create your models here.

class Projects(models.Model):
  title = models.CharField(max_length=60)
  image = models.ImageField()
  description = models.TextField()
  link = models.CharField(max_length=100)
