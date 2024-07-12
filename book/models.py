from django.db import models
from django.contrib.auth.models import User

class Emenitites(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
 
class Movie(models.Model):
    movie_name =models.CharField(max_length=100)
    movie_description = models.TextField()
    movie_image = models.CharField(max_length=500)
    price = models.IntegerField()
    emenities = models.ManyToManyField(Emenitites)
     
    def __str__(self):
        return self.movie_name