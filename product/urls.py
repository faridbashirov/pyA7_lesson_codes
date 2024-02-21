from django.urls import path
from .views import recipes,recipe_detail,like_recipe,liked_recipes
urlpatterns=[
    path("recipes",recipes,name="recipes"),
    path('recipes/<int:pk>',recipe_detail,name="recipe_detail"),
    path('like_recipe/<int:id>',like_recipe,name="like"),
    path('liked_recipes/',liked_recipes,name="likedrecipes"),


]