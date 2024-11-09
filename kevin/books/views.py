from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from .models import BooksModel, BookSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from rest_framework.pagination import LimitOffsetPagination

class ProductPagination(LimitOffsetPagination):
    default_limit = 6
    max_limit = 12
    min_limit = 1
    min_offset = 0
    max_offset = 1000000

class BooksViewSet(ModelViewSet):
    queryset = BooksModel.objects.all()
    serializer_class = BookSerializer
    pagination_class = ProductPagination

    @action(methods=["GET"], detail=False)
    def latest(self, request):
        items = self.get_queryset()[:10]
        ser = self.get_serializer_class(items, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    
    @method_decorator(cache_page(60 * 30))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @method_decorator(cache_page(60 * 30))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    


