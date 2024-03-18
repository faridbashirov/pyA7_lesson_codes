from django.urls import path
from .views import RecipeApiView,CategoryApiView
urlpatterns=[
    path("recipe/",RecipeApiView.as_view()),
    path("category/",CategoryApiView.as_view()),
]