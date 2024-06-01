from django.db import models

# Create your models here.
class Category(models.Model):
  name=models.CharField(max_length=150)
  
  def __str__(self) -> str:
    return self.name
