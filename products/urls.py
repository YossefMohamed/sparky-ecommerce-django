from django.urls import path
from .views import index , product,add_comment ,cart , add_to_cart
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('', index , name="home"),
    path("product/<int:id>" , product , name="product"),
    path("cart/<int:product_id>" , add_to_cart , name = "add_to_cart"),
    path("cart" , cart , name = "cart"),
    path("comment/<int:product_id>" , add_comment , name = "add_comment"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
