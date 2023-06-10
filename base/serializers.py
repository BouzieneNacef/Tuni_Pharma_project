from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class PannierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pannier
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommandDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommandDetails
        fields = '__all__'

class DeliveryInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryInformation
        fields = '__all__'

