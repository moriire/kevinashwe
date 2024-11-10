from rest_framework.serializers import ModelSerializer
from order.models import Order
from rest_framework.serializers import ModelSerializer, ListSerializer

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        
