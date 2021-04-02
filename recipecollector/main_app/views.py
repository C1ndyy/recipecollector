from django.shortcuts import render, redirect
from django.http import HttpResponse #<---- copy in
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe, Tool
from datetime import date
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def home(request):
    return render(request, 'about.html')

def about(request):
    return render(request, 'about.html')

@login_required
def recipes_index(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'recipes/index.html', {'recipes': recipes })

@login_required
def recipe_details(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    all_tools = Tool.objects.all()
    return render(request, 'recipes/details.html', {'recipe': recipe, 'all_tools': all_tools })

class RecipeCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = '__all__'
    success_url = '/recipes/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = '__all__'

class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = Recipe
    fields = '__all__'
    success_url = '/recipes/'

@login_required
def add_note(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    recipe.note_set.create(date=date.today(), note=request.POST['note'])
    return render(request, 'recipes/details.html', {'recipe': recipe})

@login_required
def assoc_tool(request, recipe_id):
    tool_id = request.POST['id']
    Recipe.objects.get(id=recipe_id).tools.add(tool_id)
    return redirect('details', recipe_id=recipe_id )

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)