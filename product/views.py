from django.shortcuts import render
from product.models import Recipe,Category

def recipes(request):
    recipes=Recipe.objects.all()# select * from Recipes
    category=Category.objects.all()# select * from Categories
    

    context={
        "recipes_list":recipes,
        "category_list":category
    }


    return render(request,"recipes.html",context)


# def recipe_detail(request,id):
#     recipes=Recipe.objects.get(id=id)# select * from Recipes []
#     recipes
#     category=Category.objects.all()# select * from Categories
    

#     context={
#         "recipes_list":recipes,
#         "category_list":category
#     }


#     return render(request,"recipes.html",context)



