from rest_framework import serializers
from product.models import Recipe,Category,Tag


class CategorySerializer(serializers.ModelSerializer):
    #  recipes=serializers.SerializerMethodField()
     class Meta:
        model=Category
        fields=(
            
            "title",
            "parent",
            # "recipes"
           
        )
    
    #  def get_recipes(self,obj):
    #      serializer=RecipeSerializer(obj.recipe.all(),many=True)
    #      return serializer.data

class TagSerializer(serializers.ModelSerializer):
    
     class Meta:
        model=Tag
        fields=(
            
            "title",
            
         
           
        )   

class RecipeSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    tag=TagSerializer(many=True)


    class Meta:
        model=Recipe
        fields=(
            
            "id",
            "category",
            "image",
            "title",
            "description",
            "user",
            "tag",

        )

class RecipeCreateSerializer(serializers.ModelSerializer):
 
   class Meta:
        model=Recipe
        fields=(
            
            "id",
            "category",
            "image",
            "title",
            "description",
            "user",
            "tag",

        )

