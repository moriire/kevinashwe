from rest_framework import mixins, viewsets
from .models import AppModel, AppModelSerializer

class AppModelRetrieveViewSet(mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    queryset = AppModel.objects.all()
    serializer_class = AppModelSerializer