from django.shortcuts import render,redirect
from product.models import Recipe,Category
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages

def liked_recipes(request):
    liked_recipes= request.session.get("liked_recipes","").split(",") #[1,2,3,4,5,""]
    liked_recipes.pop()
    favorites= list(map(int,liked_recipes))
    recipes=Recipe.objects.filter(id__in=favorites)# select * from Recipes
    category=Category.objects.all()
  

    context={
        "recipes_list":recipes,
        "category_list":category
    }

    return render(request,"liked_recipes.html",context)


def recipes(request):
    recipes=Recipe.objects.all()# select * from Recipes
    category=Category.objects.all()# select * from Categories
  

    context={
        "recipes_list":recipes,
        "category_list":category
    }


    return render(request,"recipes.html",context)

def recipe_detail(request,pk):
    recipe=get_object_or_404(Recipe,pk=pk)
    category=Category.objects.all()
    context={
        "recipe":recipe,
        "categories":category
    }


    return render(request,"single.html",context)



def like_recipe(request,id):
    request.session["liked_recipes"]= request.session.get("liked_recipes","") + str(id) + ","
    print(request.session["liked_recipes"])
    messages.add_message(request, messages.INFO, "Like edildi !!")
   
    return redirect(reverse_lazy("recipes"))





