from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from base.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="homepage"),
    path('store/', include('products.urls')),
    path('cart/', include('carts.urls')),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
