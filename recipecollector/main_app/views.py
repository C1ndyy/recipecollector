from django.shortcuts import render
from django.http import HttpResponse #<---- copy in

class Recipe:
    def __init__(self, name, category, link, rating):
        self.name = name
        self.category = category
        self.link =link
        self.rating =rating

recipes = [
    Recipe('Banana Bread', "Baking", "Link", 5),
    Recipe('Spagetti', "Dinner", "Link", 4),
    Recipe('Chili', "Dinner", "Link", 3),
]


# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def recipes_index(request):
    return render(request, 'recipes/index.html', {'recipes': recipes })