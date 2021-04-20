from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"pages/index.html")

def product(request):
    return render(request,"pages/productDetail.html")

def shop(request):
    return render(request,"pages/shopDetail.html")

def shoplist(request):
    return render(request,"pages/shopList.html")

def cart(request):
    return render(request,"pages/shopping-cart.html")

def shopProducts(request):
    return render(request,"pages/shopProducts.html")

def faq(request):
    return render(request,"pages/faq.html")

def contact(request):
    return render(request,"pages/contact.html")

def checkout(request):
    return render(request,"pages/check-out.html")

def blog(request):
    return render(request,"pages/blog.html")

def post(request):
    return render(request,"pages/blog-details.html")

def login(request):
    return render(request,"accounts/login.html")

def register(request):
    return render(request,"accounts/register.html")
