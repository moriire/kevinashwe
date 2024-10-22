from django.contrib import admin
from .models import AppModel
#admin.site.disable_action("delete_selected")
class AppAdmin(admin.ModelAdmin):
    actions = None
    def has_delete_permission(self, request, obj=None):
        return False
    #pass

admin.site.register(AppModel, AppAdmin)