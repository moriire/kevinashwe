from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from app_config.views import AppModelRetrieveViewSet
from books.views  import BooksViewSet
from order.views import OrderView
admin.site.site_header = 'Kevin Ashwe Books Admin'
admin.site.site_title = "Kevin Ashwe Books"
admin.site.index_title = "Kevin Ashwe Site administration"
admin.site.site_url = "https://moriire.github.io/kevin-ashwe/"
router = SimpleRouter(trailing_slash=True)
router.register(r"config", AppModelRetrieveViewSet)
router.register(r"books", BooksViewSet)
router.register("orders", OrderView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
