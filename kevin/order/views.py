from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from order.models import Order
from order.serializers import OrderSerializer
import json
class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=False, methods=["POST"])
    def payment_hook(self, request):
        data = request.data
        print(data)
        details = data["data"]
        match data["event"]:
            case 'charge.success':
                authorization_code, reference, metadata = (
                    details["authorization"].get("authorization_code"),
                    details.get("reference"), 
                    details.get("metadata")
                )
               
                items_bought = metadata.get("custom_fields")
                for item in items_bought:
                    print(item.get("id"))
                    order_obj=Order.objects.acreate(
                    created_by = metadata.get('full_name'),
                    email = metadata.get("email"),# data.get("email"),
                    reference_code = reference,
                    amount = item.get("price") / 100,
                    cart = item.get("id")
                    #city = metadata.get("city")
                )
                    order_obj.asave()   
                return Response({"data": "received"}, status=status.HTTP_201_CREATED)
            case _:
                print(data)