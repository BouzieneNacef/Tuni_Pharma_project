from rest_framework import viewsets
from .models import *
from .serializers import *

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'put', 'delete','patch']