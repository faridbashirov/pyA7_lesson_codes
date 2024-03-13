from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from product.models import Recipe,Category
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.views.generic.edit import FormMixin
from .forms import RecipeReviewForm,RecipeCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
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

class RecipesView(LoginRequiredMixin,ListView):
    template_name="recipes.html"
    model=Recipe
    context_object_name="recipes_list"
    paginate_by=1

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["category_list"]=Category.objects.all()
        return context
    
    def get_queryset(self):
        queryset=super().get_queryset()
        category=self.request.GET.get("category")
        tag=self.request.GET.get("tag")

        if category and tag :
            
            queryset=Recipe.objects.filter(category__title=category,tag__title=tag)
            
        
        return queryset




def recipe_detail(request,pk):
    recipe=get_object_or_404(Recipe,pk=pk)
    category=Category.objects.all()
    context={
        "recipe":recipe,
        "categories":category
    }


    return render(request,"single.html",context)

class RecipeDetailView(FormMixin,DetailView):
     template_name="single.html"
     model=Recipe
     form_class = RecipeReviewForm

   

     def get_success_url(self):
        return reverse_lazy("recipe_detail", kwargs={"slug": self.object.slug})
     

     def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
     def form_valid(self, form):
        form.instance.user=self.request.user
        form.instance.recipe=self.get_object()
        form.save()

        return super().form_valid(form)
    
     def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["categories"]=Category.objects.all()
        return context




def like_recipe(request,id):
    request.session["liked_recipes"]= request.session.get("liked_recipes","") + str(id) + ","
    print(request.session["liked_recipes"])
    messages.add_message(request, messages.INFO, "Like edildi !!")
   
    return redirect(reverse_lazy("recipes"))



class RecipeCreateView(CreateView):
    model=Recipe
    template_name="create_story.html"
    form_class=RecipeCreateForm
    success_url=reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        # form.instance.recipe=self.get_object()
        form.save()

        return super().form_valid(form)
    
    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, "Like edildi !!")
        return super().get_success_url()

class RecipeUpdateView(UpdateView):
     template_name="update_recipe.html"
 


