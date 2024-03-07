
from django import forms
from .models import RecipeReview,Recipe

class RecipeReviewForm(forms.ModelForm):

     class Meta:
          model=RecipeReview
          fields=("message",)
          widgets={
            "message":forms.Textarea(attrs={
                "class":"form-control",
                "placeholder":"Your message"
            }),
           }
          
class RecipeCreateForm(forms.ModelForm):
      
      class Meta:
          model=Recipe
          fields=('title','small_description','description','image','category','tag')

