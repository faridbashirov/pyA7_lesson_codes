from rest_framework.views import APIView
from django.http import JsonResponse
from product.models import Recipe,Category
from .serializers import RecipeSerializer,CategorySerializer,RecipeCreateSerializer
class RecipeApiView(APIView):
    
    def get(self, request, *args, **kwargs):
        recipe=Recipe.objects.all()
        serializer=RecipeSerializer(recipe,context={"request":request},many=True)

        
        return JsonResponse(data=serializer.data,safe=False)
    
    def post(self, request, *args, **kwargs):
         post_data=request.data

         serializer=RecipeCreateSerializer(data=post_data)
         if serializer.is_valid():
             serializer.save()
             return JsonResponse(data=serializer.data,status=201)
         return JsonResponse(serializer.errors)




    
    
class CategoryApiView(APIView):
    
    def get(self, request, *args, **kwargs):
        category=Category.objects.all()
        serializer=CategorySerializer(category,many=True)

        
        return JsonResponse(data=serializer.data,safe=False)
    

    
        




