from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('recipes/', views.recipes_index, name='index'),
    path('recipes/<int:recipe_id>/', views.recipe_details, name='details'),
    path('recipes/create/', views.RecipeCreate.as_view(), name="recipe_create"),
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name="recipe_update"),
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name="recipe_delete"),
    path('recipes/<int:recipe_id>/add_note/', views.add_note, name='add_note'),
    path('recipes/<int:recipe_id>/assoc_tool', views.assoc_tool, name='assoc_tool'),
]