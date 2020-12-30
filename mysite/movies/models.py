from django.db import models

# Create your models here.
class Title(models.Model):
  title = models.CharField(max_length=200)
  year = models.IntegerField()
  description = models.TextField()
