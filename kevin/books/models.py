from django.db import models
from rest_framework.serializers import ModelSerializer
from django.utils.translation import gettext_lazy as _
from utils import image_resize
import uuid
def book_image_path(instance, filename):
    return '/'.join(["-".join(instance.title.split()), filename])
    
class BooksModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cover = models.ImageField(_("Book Cover Page Image"), upload_to=book_image_path)
    title = models.CharField(max_length=32)
    price = models.FloatField(default=0.0)
    subtitle = models.CharField(max_length=64)
    description = models.TextField(default="")
    created_on = models.DateTimeField(auto_now=True)
    modified_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.cover.file:
            image_resize(self.cover, 500, 650)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.cover:
            self.cover.delete(save=True)
        super(BooksModel, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"


class BookSerializer(ModelSerializer):
    class Meta:
        model = BooksModel
        fields = "__all__"
