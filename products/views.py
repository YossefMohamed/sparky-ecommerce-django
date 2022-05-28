from django.shortcuts import render
from .models import Product , Comment
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse



def index(request):
    products = Product.objects.order_by("-date")
    print( products[0].name)
    return render(request, 'index.html' , {
        "products" : products
    })


def product(request, id):
    try:
        product = Product.objects.get(id=id)
        comments = product.comments.all()
    except Product.DoesNotExist:
        return render(request, '404.html')

    return render(request, 'product.html' , {
            "product" : product,
            "comments" : comments
        })



@require_http_methods(["POST"])
def add_comment(request , product_id):
    comment = Comment()
    comment.user = 1
    comment.product = product_id
    comment.text = request.POST["comment"]
    comment.rate = request.POST["rate"]
    comment = comment.save()
    return HttpResponseRedirect(reverse("product", kwargs={"id": 1}))
