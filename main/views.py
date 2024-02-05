from django.shortcuts import render
from .models import Food
from main.serializers import FoodSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class FoodView(APIView):
    def get(self, request):
        foods = Food.objects.all()
        serializer_data = FoodSerializer(foods, many=True)
        return Response( {"foods":serializer_data.data} )
    
    @csrf_exempt
    def post(self, request):
        serializer_data = FoodSerializer( data=request.data )
        if serializer_data.is_valid():
            food = serializer_data.save()
            # food.adder = request.user
            # food.save()
            return Response( {"status":"ok"} )
        return Response( {"status":"error","detail":serializer_data.errors } )


class FoodDetailView(APIView):
    def get(self, request,id):
        food = Food.objects.filter(id=id)
        if food:
            serializer_data = FoodSerializer(food[0])
            return Response( {"food":serializer_data.data} )    
        return Response( {"status":"error"," detail":"Object not found "} )  
   
    def put(self, request,id):
        food = Food.objects.filter(id=id)
        if food:
            food = food[0]
            title = request.data.get('title', food.title)
            volume = request.data.get('volume' ,  food.volume)
            kkl = request.data.get('kkl' ,food.kkl )
            food.title = title    
            food.volume = volume    
            food.kkl = kkl    
            food.save()
            serializer_data = FoodSerializer(food)
            return Response( {"food":serializer_data.data} )    
        return Response( {"status":"error"," detail":"Object not found "} )    


    def delete(self, request,id):
        try:
            food = Food.objects.get(id=id)
            food.delete()
            return Response( {"status":"deleted"} )
        except:    
            return Response( {"status":"error"," detail":"Object not found "} ) 

