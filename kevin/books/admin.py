from django.contrib import admin
from .models import BooksModel
class AppAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "price", "created_on", "modified_on")
    #pass

admin.site.register(BooksModel, AppAdmin)