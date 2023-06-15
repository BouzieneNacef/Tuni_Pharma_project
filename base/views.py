from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from .models import *
from .serializers import*





# Customizing token claims: 
# un sérialiseur de jeton personnalisé et une vue pour obtenir des paires de jetons dans Django REST Framework
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username  
        # ...

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/token',
        '/token/refresh',
    ]

    return Response(routes)

# Product CRUD:

# add product
@api_view(['POST'])
def add_product(request):
    if request.method=='POST':
        product=ProductSerializer(data=request.data) #get the product object from the request after deserialization
        if product.is_valid(): #check if the product object is valid (all required fields are filled and fields data types and format are correct)
            product.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(product.errors,status=status.HTTP_400_BAD_REQUEST)
   
    return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)

# get all of the product
@api_view(['GET'])
def get_all_product(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# retreive, update and delete product            
@api_view(['GET','PUT','DELETE'])
def retreive_update_or_delete_product(request,id):
        try:
            product=Product.objects.get(pk=id)
            if request.method=='GET':
    
                serializer=ProductSerializer(product)
                return Response(serializer.data,status=status.HTTP_200_OK)
       
            elif request.method=='PUT':
              serialzer=ProductSerializer(product,data=request.data)#get group informations from the request and update the instance of group geted by nid from the DB.
              if serialzer.is_valid():
                serialzer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
              return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)
            elif request.method=='DELETE':
                product.delete()
                return Response(status=status.HTTP_204_NO_CONTENT) # to say that the deleted group no longer exists
                #or
                #return JsonResponse({"message":"The group was successuflly deleted"},status=status.HTTP_202_ACCEPTED)
            return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


# command crud:

@api_view(['POST'])
def add_command(request):
    if request.method=='POST':
        command=CommandSerializer(data=request.data) #get the comand object from the request after deserialization
        if command.is_valid(): #check if the command object is valid (all required fields are filled and fields data types and format are correct)
            command.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(command.errors,status=status.HTTP_400_BAD_REQUEST)
   
    return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
# retreive, update and delete command            
@api_view(['GET','PUT','DELETE'])
def retreive_update_or_delete_command(request,id):
        try:
            command=Command.objects.get(pk=id)
            if request.method=='GET':
    
                serializer=CommandSerializer(command)
                return Response(serializer.data,status=status.HTTP_200_OK)
       
            elif request.method=='PUT':
              serialzer=CommandSerializer(command,data=request.data)#get group informations from the request and update the instance of group geted by nid from the DB.
              if serialzer.is_valid():
                serialzer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
              return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)
            elif request.method=='DELETE':
                command.delete()
                return Response(status=status.HTTP_204_NO_CONTENT) # to say that the deleted group no longer exists
                #or
                #return JsonResponse({"message":"The group was successuflly deleted"},status=status.HTTP_202_ACCEPTED)
            return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        except Command.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
@api_view(['GET'])
def get_all_command(request):
    command = Command.objects.all()
    serializer = CommandSerializer(command, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

