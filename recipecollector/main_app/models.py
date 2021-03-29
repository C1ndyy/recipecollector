from django.db import models

# Create your models here
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    rating = models.IntegerField()

    def __str__(self):
        return self.name
