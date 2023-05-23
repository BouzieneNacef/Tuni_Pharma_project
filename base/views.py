from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from .models import *
from .serializers import*



# {
# "token_type": "access",
# "exp": 1684071855,
#"iat": 1684071555,
#"jti": "618c3748d49f4114bfd7c5ab969fc80d",
#"user_id": 1,
#"username": "user01"  *****
#}


# Customizing token claims: 
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



