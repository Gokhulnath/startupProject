from django.shortcuts import render
from shop.models import Advertisement, Shop, Product

# Create your views here.
def index(request):
    ads = Advertisement.objects.filter(is_published=True).order_by('-list_date')[:2]
    if len(ads)==2:
        ad_shop_1 = Shop.objects.get(id=ads[0].shop.id)
        ad_products_1 = Product.objects.filter(shop=ads[0].shop.id).filter(is_published=True).order_by('-list_date')
        ad_shop_2 = Shop.objects.get(id=ads[1].shop.id)
        ad_products_2 = Product.objects.filter(shop=ads[1].shop.id).filter(is_published=True).order_by('-list_date')
        context ={ 'ad_shop_1':ad_shop_1, 'ad_products_1':ad_products_1, 'ad_shop_2':ad_shop_2, 'ad_products_2':ad_products_2}
        return render(request,"pages/index.html", context)
    else:
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
