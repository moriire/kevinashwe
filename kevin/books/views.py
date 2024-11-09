from rest_framework.viewsets import ModelViewSet
from .models import BooksModel, BookSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

class BooksViewSet(ModelViewSet):
    queryset = BooksModel.objects.all()
    serializer_class = BookSerializer

    @method_decorator(cache_page(60 * 30))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @method_decorator(cache_page(60 * 30))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    


