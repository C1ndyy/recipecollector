from django.db import models
from django.urls import reverse

# Create your models here

RATINGS = ((1,1),(2,2),(3,3),(4,4),(5,5))
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    rating = models.IntegerField(
        choices=RATINGS,
        default=RATINGS[0]
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('details', kwargs={'recipe_id': self.id})


class Note(models.Model):
    date = models.DateField()
    note = models.TextField(max_length=500)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.note