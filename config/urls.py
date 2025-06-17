from django.contrib import admin
from django.urls import path, include
from django.views import defaults as default_views
from django.conf import settings
from django.contrib.auth.models import User
from django.conf.urls.static import static


urlpatterns = [
    path("", include("rutuvia_apps.pages.urls", namespace="pages")),
    path("", include("rutuvia_apps.account.urls", namespace="account")),
    path("", include("rutuvia_apps.product.urls", namespace="product")),
    path("", include("rutuvia_apps.cart.urls", namespace="cart"))
]

urlpatterns += [
    path(settings.ADMIN_URL, admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
