from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from order.models import Order
from order.serializers import OrderSerializer

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
                    order_obj=Order(
                    created_by = f"{metadata.get('full_name')}",
                    by_email = metadata.get("email"),# data.get("email"),
                    reference_code = reference,
                    amount = details.get("amount")/100,
                    cart = items_bought.id
                    #city = metadata.get("city")
                )
                    order_obj.asave()   
                return Response({"data": "received"}, status=status.HTTP_201_CREATED)
            case _:
                print(data)