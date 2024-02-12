from django.shortcuts import render
from product.models import Recipe,Category
from django.shortcuts import get_object_or_404

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


# def recipe_detail(request,id):
#     recipes=Recipe.objects.get(id=id)# select * from Recipes []
#     recipes
#     category=Category.objects.all()# select * from Categories
    

#     context={
#         "recipes_list":recipes,
#         "category_list":category
#     }


#     return render(request,"recipes.html",context)



