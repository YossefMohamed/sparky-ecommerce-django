from email import message
from statistics import quantiles
from django.shortcuts import render
from .models import Product , Comment , User , Cart
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse


def index(request):
    products = Product.objects.order_by("-date")
    print( products[0].name)
    return render(request, 'index.html' , {
        "products" : products
    })


def product(request, id , message=""):
    try:
        product = Product.objects.get(id=id)
        comments = product.comments.all().order_by("-date")
    except Product.DoesNotExist:
        return render(request, '404.html' ,{
             "messages" : {
                 "tag" : "danger",
            "message" : "Product not found"
        }
        })
    return render(request, 'product.html' , {
            "product" : product,
            "comments" : comments
        })

@require_http_methods(["POST"])
def add_comment(request , product_id):
    # try:
    user = User.objects.get(id=1)
    comment = Comment()
    comment.user = user
    comment.product = Product.objects.get(id=product_id)
    comment.text = request.POST["comment"]
    comment.rate = request.POST["rating"]
    comment = comment.save()
    # except KeyError:
    #     return render(reverse("product", kwargs={"id":product_id ,    "messages" : {
    #              "tag" : "danger",
    #         "message" : "Product not found"
    #     }}))
    return HttpResponseRedirect(reverse("product", kwargs={"id": product_id}))


@require_http_methods(["POST"])
def add_to_cart(request , product_id):
    cart = Cart()
    cart.user = User.objects.get(id=1)
    cart.product = Product.objects.get(id=product_id)
    import json
    body = json.loads(request.body)
    cart.quantity = body["quantity"]
    cart = cart.save()
    return JsonResponse({"message" : "Product added to cart"})




def cart(request):
    try:
        user = User.objects.get(id=1)
        cart = Cart.objects.filter(user=user)
        return render(request , "cart.html" , {
       "carts" : cart 
             })
    except User.DoesNotExist or Cart.DoesNotExist:
        return render(request , "cart.html")
   
