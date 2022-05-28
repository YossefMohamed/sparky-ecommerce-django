from django.urls import path
from .views import index , product,add_comment

urlpatterns = [
        path('', index , name="home"),
    path("product/<int:id>" , product , name="product"),
    path("comment/<int:product_id>" , add_comment , name = "add_comment"),


]