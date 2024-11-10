from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
      list_display = ("created_by", "carts", "mode", "address", "status", "amount")
      ordering = ('-created_on',)
      search_fields = ('created_by',)

      @admin.display(description='items')
      def carts(self, obj):
            return [item.name for item in obj.cart.all()]

admin.site.register(Order)#, OrderAdmin)