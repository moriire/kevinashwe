from rest_framework.viewsets import ModelViewSet
from .models import BooksModel, BookSerializer

class BooksViewSet(ModelViewSet):
    queryset = BooksModel.objects.all()
    serializer_class = BookSerializer