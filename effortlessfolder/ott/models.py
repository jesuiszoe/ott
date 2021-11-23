from django.db import models

# Create your models here.
class Netflix(models.Model):
    type = models.CharField(max_length=200)
    title = models.CharField(max_length=50, unique =True)
    director =  models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    release_year = models.IntegerField()
    rating = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    listed_in = models.CharField(max_length=200)
    description= models.TextField()

    def __str__(self):
        return self.title

class Hulu(models.Model):
    pass
    

class Amazon(models.Model):
    pass
    

class Disney(models.Model):
    pass
    
