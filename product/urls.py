from django.urls import path
from .views import recipes,recipe_detail,like_recipe,liked_recipes,RecipesView,RecipeDetailView,RecipeCreateView,RecipeUpdateView
urlpatterns=[
    path("recipes",RecipesView.as_view(),name="recipes"),
    path('recipes/<slug:slug>',RecipeDetailView.as_view(),name="recipe_detail"),
    path('like_recipe/<int:id>',like_recipe,name="like"),
    path('liked_recipes/',liked_recipes,name="likedrecipes"),
    path("create_recipe/",RecipeCreateView.as_view(),name="create_recipe"),
    path("update_recipe/<int:pk>",RecipeUpdateView.as_view(),name="recipe_update")


]