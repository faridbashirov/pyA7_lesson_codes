from django.urls import path
from .views import recipes,recipe_detail
urlpatterns=[
    path("recipes",recipes,name="recipes"),
    path('recipes/<int:pk>',recipe_detail,name="recipe_detail")

]