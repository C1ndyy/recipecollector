from django.shortcuts import render, redirect
from django.http import HttpResponse #<---- copy in
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe, Tool
from datetime import date


# Create your views here.
def home(request):
    return render(request, 'about.html')

def about(request):
    return render(request, 'about.html')

def recipes_index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes': recipes })

def recipe_details(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    all_tools = Tool.objects.all()
    return render(request, 'recipes/details.html', {'recipe': recipe, 'all_tools': all_tools })

class RecipeCreate(CreateView):
    model = Recipe
    fields = '__all__'
    success_url = '/recipes/'

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = '__all__'

class RecipeDelete(DeleteView):
    model = Recipe
    fields = '__all__'
    success_url = '/recipes/'

def add_note(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    recipe.note_set.create(date=date.today(), note=request.POST['note'])
    return render(request, 'recipes/details.html', {'recipe': recipe})

def assoc_tool(request, recipe_id):
    tool_id = request.POST['id']
    Recipe.objects.get(id=recipe_id).tools.add(tool_id)
    return redirect('details', recipe_id=recipe_id )