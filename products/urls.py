from django.urls import path
from .views import index , product,add_comment ,search,product_with_cat,cart , profile ,not_found ,  add_to_cart ,login , logout,register
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index , name="home"),
    path("product/<int:id>" , product , name="product"),
    path("product/<cat>" , product_with_cat , name="product_with_cat"),
    path("cart/<int:product_id>" , add_to_cart , name = "add_to_cart"),
    path("cart" , cart , name = "cart"),
    path("login" , login , name = "login"),
    path("logout" , logout , name = "logout"),
    path("register" , register , name = "register"),
    path("comment/<int:product_id>" , add_comment , name = "add_comment"),
    path("search" , search , name = "search"),
    path("profile" , profile , name = "profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


