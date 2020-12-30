from django.db import models

# Create your models here.
class Title(models.Model):
  title = models.TextField()
  year = models.IntegerField()
  description = models.TextField()

  def __str__(self):
    return self.title
