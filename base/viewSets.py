from rest_framework import viewsets
from .models import *
from .serializers import *

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'put', 'delete','patch']

class CommandViewSet(viewsets.ModelViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer
    http_method_names = ['get', 'post', 'put', 'delete','patch']



class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    http_method_names = ['get', 'post', 'put', 'delete','patch']

class CommandDetailsViewSet(viewsets.ModelViewSet):
    queryset = CommandDetails.objects.all()
    serializer_class = CommandDetailsSerializer
    http_method_names = ['get', 'post', 'put', 'delete','patch']

class DeliveryInformationViewSet(viewsets.ModelViewSet):
    queryset = DeliveryInformation.objects.all()
    serializer_class = DeliveryInformationSerializer
    http_method_names = ['get', 'post', 'put', 'delete','patch']
   

class PannierViewSet(viewsets.ModelViewSet):
      queryset = Pannier.objects.all()
      serializer_class = PannierSerializer
      http_method_names = ['get', 'post', 'put']

class CategoryViewSet(viewsets.ModelViewSet):
      queryset = Category.objects.all()
      serializer_class = CategorySerializer
      http_method_names = ['get', 'post', 'put', 'delete','patch']





