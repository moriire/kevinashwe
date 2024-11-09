from rest_framework import mixins, viewsets
from .models import AppModel, AppModelSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

class AppModelRetrieveViewSet(mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    queryset = AppModel.objects.all()
    serializer_class = AppModelSerializer

    @method_decorator(cache_page(60 * 30))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)