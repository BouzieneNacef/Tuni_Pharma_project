from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from .models import Product,Command, Client, DeliveryInformation, Pannier, CommandDetails,Category
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

# get the product by name
@api_view(['GET'])
def filter_products_by_name(request):
    name = request.GET.get('name', '')

    # Perform the filtering
    products = Product.objects.filter(name__icontains=name)
    
    # Serialize the filtered products
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)

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
def retreive_update_or_delete_command(self,request,id):
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

# add client
@api_view(['POST'])
def add_client(request):
    if request.method=='POST':
        client=ClientSerializer(data=request.data) 
        if client.is_valid(): 
            return Response(status=status.HTTP_201_CREATED)
        return Response(client.errors,status=status.HTTP_400_BAD_REQUEST)
   
    return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
# retreive, update and delete client           
@api_view(['GET','PUT','DELETE'])
def retreive_update_or_delete_client(request,id):
        try:
            client=Client.objects.get(pk=id)
            if request.method=='GET':
                serializer=ClientSerializer(client)
                return Response(serializer.data,status=status.HTTP_200_OK)
       
            elif request.method=='PUT':
              serialzer=ClientSerializer(client,data=request.data)#get group informations from the request and update the instance of group geted by nid from the DB.
              if serialzer.is_valid():
                serialzer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
              return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)
            elif request.method=='DELETE':
                client.delete()
                return Response(status=status.HTTP_204_NO_CONTENT) 
            return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
# add pannier
@api_view(['POST'])
def add_pannier(request):
    if request.method=='POST':
        pannier=PannierSerializer(data=request.data) 
        if pannier.is_valid(): 
            return Response(status=status.HTTP_201_CREATED)
        return Response(pannier.errors,status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
# retreive, update and delete cpannier           
@api_view(['GET','PUT','DELETE'])
def retreive_update_or_delete_pannier(request,id):
        try:
            pannier=Pannier.objects.get(pk=id)
            if request.method=='GET':
                serializer=PannierSerializer(pannier)
                return Response(serializer.data,status=status.HTTP_200_OK)
       
            elif request.method=='PUT':
              serialzer=PannierSerializer(pannier,data=request.data)#get group informations from the request and update the instance of group geted by nid from the DB.
              if serialzer.is_valid():
                serialzer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
              return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)
            elif request.method=='DELETE':
                pannier.delete()
                return Response(status=status.HTTP_204_NO_CONTENT) 
            return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        except Pannier.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


# add command details
@api_view(['POST'])
def add_details(request):
    if request.method=='POST':
        details=CommandDetailsSerializer(data=request.data) 
        if details.is_valid(): 
            return Response(status=status.HTTP_201_CREATED)
        return Response(details.errors,status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
# retreive, update and delete commant details         
@api_view(['GET','PUT','DELETE'])
def retreive_update_or_delete_details(request,id):
        try:
            details=CommandDetails.objects.get(pk=id)
            if request.method=='GET':
                serializer=CommandDetailsSerializer(details)
                return Response(serializer.data,status=status.HTTP_200_OK)
       
            elif request.method=='PUT':
              serialzer=CommandDetailsSerializer(details,data=request.data)#get group informations from the request and update the instance of group geted by nid from the DB.
              if serialzer.is_valid():
                serialzer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
              return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)
            elif request.method=='DELETE':
                details.delete()
                return Response(status=status.HTTP_204_NO_CONTENT) 
            return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        except CommandDetails.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

# add delivery
@api_view(['POST'])
def add_delivery(request):
    if request.method=='POST':
        delivery=DeliveryInformationSerializer(data=request.data) 
        if delivery.is_valid(): 
            return Response(status=status.HTTP_201_CREATED)
        return Response(delivery.errors,status=status.HTTP_400_BAD_REQUEST)
   
    return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
# retreive, update and delete delivery           
@api_view(['GET','PUT','DELETE'])
def retreive_update_or_delete_delivery(request,id):
        try:
            delivery=DeliveryInformation.objects.get(pk=id)
            if request.method=='GET':
                serializer=DeliveryInformationSerializer(delivery)
                return Response(serializer.data,status=status.HTTP_200_OK)
       
            elif request.method=='PUT':
              serialzer=DeliveryInformationSerializer(delivery,data=request.data)#get group informations from the request and update the instance of group geted by nid from the DB.
              if serialzer.is_valid():
                serialzer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
              return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)
            elif request.method=='DELETE':
                delivery.delete()
                return Response(status=status.HTTP_204_NO_CONTENT) 
            return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        except DeliveryInformation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


# add category
@api_view(['POST'])
def add_category(request):
    if request.method=='POST':
        category=CategorySerializer(data=request.data) 
        if category.is_valid(): 
            return Response(status=status.HTTP_201_CREATED)
        return Response(category.errors,status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
# retreive, update and delete category          
@api_view(['GET','PUT','DELETE'])
def retreive_update_or_delete_category(request,id):
        try:
            category = Category.objects.get(pk=id)
            if request.method=='GET':
                serializer=CategorySerializer(category)
                return Response(serializer.data,status=status.HTTP_200_OK)
       
            elif request.method=='PUT':
              serialzer=CategorySerializer(category,data=request.data)#get group informations from the request and update the instance of group geted by nid from the DB.
              if serialzer.is_valid():
                serialzer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
              return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)
            elif request.method=='DELETE':
                category.delete()
                return Response(status=status.HTTP_204_NO_CONTENT) 
            return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)






'''

class ClientView(APIView):
    # add client 
    @api_view(['POST'])
    def add_client(self,request):
        if request.method == 'POST':
            client = ClientSerializer(data=request.data)
            if client.is_valid():
                client.save()
                return Response(status=status.HTTP_201_CREATED)
            return Response(client.errors, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    # retreive, update and delete client 
    @api_view(['GET','PUT','DELETE'])
    def retreive_update_or_delete_client(self,request,id):
        try:
            client=Client.objects.get(pk=id)
            # GET method
            if request.method=='GET':
                serializer=ClientSerializer(client)
                return Response(serializer.data,status=status.HTTP_200_OK)
            # PUT method
            elif request.method=='PUT':
              serialzer=ClientSerializer(client,data=request.data)#get group informations from the request and update the instance of group geted by nid from the DB.
              if serialzer.is_valid():
                serialzer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
              return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)
            # DELETE method
            elif request.method=='DELETE':
                client.delete()
                return Response(status=status.HTTP_204_NO_CONTENT) # to say that the deleted group no longer exists
            return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class Category(APIView):
    # add category 
    @api_view(['POST'])
    def add_category(self,request):
        if request.method == 'POST':
            category = CategorySerializer(data=request.data)
            if category.is_valid():
                category.save()
                return Response(status=status.HTTP_201_CREATED)
            return Response(category.errors, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    # retreive, update and delete category
    @api_view(['GET','PUT','DELETE'])
    def retreive_update_or_delete_category(self,request,id):
        try:
            category=Category.objects.get(pk=id)
            # GET method
            if request.method=='GET':
                serializer=CategorySerializer(category)
                return Response(serializer.data,status=status.HTTP_200_OK)
            # PUT method
            elif request.method=='PUT':
              serialzer=CategorySerializer(category,data=request.data)#get group informations from the request and update the instance of group geted by nid from the DB.
              if serialzer.is_valid():
                serialzer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
              return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)
            # DELETE method
            elif request.method=='DELETE':
                category.delete()
                return Response(status=status.HTTP_204_NO_CONTENT) # to say that the deleted group no longer exists
            return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class CommandDetails(APIView):
    # add details 
    @api_view(['POST'])
    def add_details(self,request):
        if request.method == 'POST':
            details = CommandDetailsSerializer(data=request.data)
            if details.is_valid():
                details.save()
                return Response(status=status.HTTP_201_CREATED)
            return Response(details.errors, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    # retreive, update and delete details 
    @api_view(['GET','PUT','DELETE'])
    def retreive_update_or_delete_details(self,request,id):
        try:
            details=CommandDetails.objects.get(pk=id)
            # GET method
            if request.method=='GET':
                serializer=CommandDetailsSerializer(details)
                return Response(serializer.data,status=status.HTTP_200_OK)
            # PUT method
            elif request.method=='PUT':
              serialzer=CommandDetailsSerializer(details,data=request.data)#get group informations from the request and update the instance of group geted by nid from the DB.
              if serialzer.is_valid():
                serialzer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
              return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)
            # DELETE method
            elif request.method=='DELETE':
                details.delete()
                return Response(status=status.HTTP_204_NO_CONTENT) # to say that the deleted group no longer exists
            return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        except CommandDetails.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class DeliveryInformation(APIView):
    # add delivery
    @api_view(['POST'])
    def add_delivery(self,request):
        if request.method == 'POST':
            delivery = DeliveryInformationSerializer(data=request.data)
            if delivery.is_valid():
                delivery.save()
                return Response(status=status.HTTP_201_CREATED)
            return Response(delivery.errors, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    # retreive, update and delete delivery 
    @api_view(['GET','PUT','DELETE'])
    def retreive_update_or_delete_delivery(self,request,id):
        try:
            delivery=DeliveryInformation.objects.get(pk=id)
            # GET method
            if request.method=='GET':
                serializer=DeliveryInformationSerializer(delivery)
                return Response(serializer.data,status=status.HTTP_200_OK)
            # PUT method
            elif request.method=='PUT':
              serialzer=DeliveryInformationSerializer(delivery,data=request.data)#get group informations from the request and update the instance of group geted by nid from the DB.
              if serialzer.is_valid():
                serialzer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
              return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)
            # DELETE method
            elif request.method=='DELETE':
                delivery.delete()
                return Response(status=status.HTTP_204_NO_CONTENT) # to say that the deleted group no longer exists
            return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        except DeliveryInformation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class PannierView(APIView):
    # add pannier 
    @api_view(['POST'])
    def add_pannier(self,request):
        if request.method == 'POST':
            pannier = PannierSerializer(data=request.data)
            if pannier.is_valid():
                pannier.save()
                return Response(status=status.HTTP_201_CREATED)
            return Response(pannier.errors, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    # retreive, update and delete pannier 
    @api_view(['GET','PUT','DELETE'])
    def retreive_update_or_delete_pannier(self,request,id):
        try:
            pannier=Pannier.objects.get(pk=id)
            # GET method
            if request.method=='GET':
                serializer=PannierSerializer(pannier)
                return Response(serializer.data,status=status.HTTP_200_OK)
            # PUT method
            elif request.method=='PUT':
              serialzer=PannierSerializer(pannier,data=request.data)#get group informations from the request and update the instance of group geted by nid from the DB.
              if serialzer.is_valid():
                serialzer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
              return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)
            # DELETE method
            elif request.method=='DELETE':
                pannier.delete()
                return Response(status=status.HTTP_204_NO_CONTENT) # to say that the deleted group no longer exists
            return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        except Pannier.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        



'''







