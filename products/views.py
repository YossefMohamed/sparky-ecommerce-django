from email import message
from statistics import quantiles
from django.shortcuts import render
from .models import Product , Comment , CustomerUser , Cart
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Count


login_required   =   login_required ( login_url = "login" )


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home"))
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            auth_login(request,user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, 'login.html' , {
                "messages" : {
                    "tag" : "danger",
                    "message" : "Invalid username or password"
                }
            })
    return render(request, 'login.html')

def index(request):
    
    products = Product.objects.order_by("-date")[0:9] # [offset : limit]
    # get new products
    new_products = products[:3]
    return render(request, 'index.html' , {
        "products" : products,
        "new_products" : new_products
    })


def product(request, id):
    try:
        product = Product.objects.get(id=id)
        print(product)
        comments = product.comments.all().order_by("-date")
        rate = 0
        for comment in comments:
            rate += comment.rate
        if len(comments) == 0 :
            rate = 0;
        else:
            rate = rate / len(comments)
        print(rate)
    except Product.DoesNotExist:
        return render(request, '404.html' ,{
             "messages" : {
                 "tag" : "danger",
            "message" : "Product not found"
        }
        })
        
    return render(request, 'product.html' , {
            "product" : product,
            "comments" : comments,
            "rate" : range(int(rate))
        })

@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("home"))




@login_required
@require_http_methods(["POST"])
def add_comment(request , product_id):
    comment = Comment()
    comment.user = request.user
    comment.product = Product.objects.get(id=product_id)
    comment.text = request.POST["comment"]
    comment.rate = request.POST["rating"]
    comment = comment.save()
    return HttpResponseRedirect(reverse("product", kwargs={"id": product_id}))

@login_required
@require_http_methods(["POST"])
def add_to_cart(request , product_id):
    cart = Cart()
    cart.user = request.user
    cart.product = Product.objects.get(id=product_id)
    import json
    body = json.loads(request.body)
    cart.quantity = body["quantity"]
    cart = cart.save()
    return JsonResponse({"message" : "Product added to cart"})



@login_required
def cart(request):
    if request.method == "POST":
        id = request.POST["cart"]
        print(id)
        cart = Cart.objects.filter(id=id).delete()
        cart = Cart.objects.filter(user=request.user)
        total =0
        for ca in cart:
            total+= ca.product.price * ca.quantity
        return JsonResponse({"total" : total})

    else:
        try:
            cart = Cart.objects.filter(user=request.user)
            total =0
            for ca in cart:
                total+= ca.product.price * ca.quantity
            return render(request , "cart.html" , {
        "carts" : cart ,
       "carts_length" : len(cart) ,
       "total" : total
                })
        except CustomerUser.DoesNotExist or Cart.DoesNotExist:
             return HttpResponseRedirect(render(request , "cart.html"))
   


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home"))
    if request.method == "POST" :
        try:
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            user = CustomerUser.objects.create_user(username, email, password)
            user.save()
            logout(request)
            return HttpResponseRedirect(reverse("login"))
        except Exception as e:
            return render(request , "register.html" , {"messages" : {
                "tag" : "danger",
                "message" : str(e) 
            }})

    return render(request , "register.html")






@login_required
def profile(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        request.user.email = email
        if 'image' in request.FILES.keys():
            request.user.image = request.FILES["image"]
        request.user.username = username
        request.user.save()
        print(request.user.password)
        return render(request , "profile.html" , {"image" : request.user.image.url,"name" : request.user.username , "email" : request.user.email }) 

    return render(request , "profile.html" , {"image" : request.user.image.url,"name" : request.user.username , "email" : request.user.email }) 








def not_found(request):
    return render(request , "404.html")

def product_with_cat(request,cat):
    cats = ["phones" , "laptops" , "tablets" , "accessories"]
    if cat.lower() in cats:
        if 'pages' in request.GET.keys():
            current_page = int(request.GET["pages"]) -1
        else:
            current_page = 1 -1
        if current_page == 0 :
            skip = 0
        else:
            skip = (current_page * 9) -1 
        products = Product.objects.filter(category=cat.lower())[skip:9]
        products_number = Product.objects.filter(category=cat.lower()).count()
        import math
        pages = math.ceil(products_number/9)

        return render(request , "products-with-cat.html" , {
            "cat" : cat.lower(),
            "products" : products,
            "pages" : pages,
            "current_page" : current_page +1
        })
    else : 
        return HttpResponseRedirect(reverse("home"))




def search(request):
    print(request.GET["tag"])
    if 'pages' in request.GET.keys():
        current_page = int(request.GET["pages"]) -1
    else:
        current_page = 1 -1
    if current_page == 0 :
        skip = 0
    else:
        skip = (current_page * 9) -1    
    products = Product.objects.filter(name__contains=request.GET["tag"])[skip:9]
    products_number = Product.objects.filter(name__contains=request.GET["tag"]).count()
    import math
    pages = math.ceil(products_number/9)

    return render(request , "products-with-search.html" , {
            "cat" : request.GET["tag"],
            "products" : products,
            "pages" : pages,
            "current_page" : current_page +1
        })