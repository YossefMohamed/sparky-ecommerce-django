from django.contrib import admin
from .models import Product , Cart,CustomerUser , Comment



admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CustomerUser)
admin.site.register(Comment)