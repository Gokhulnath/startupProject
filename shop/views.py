from django.shortcuts import render
from .models import Shop, Product


def shop(request, shop):
    shop_detail = Shop.objects.get(slug=shop)
    context = {'shop':shop_detail}
    return render(request,"pages/shopDetail.html", context)

def shoplist(request):
    shopList = Shop.objects.filter(is_published=True).order_by('-list_date')
    context={'shopList':shopList}
    return render(request,"pages/shopList.html", context)


def shopProducts(request):
    productList = Product.objects.filter(is_published=True).order_by('-list_date')
    context={'productList':productList}
    return render(request,"pages/shopProducts.html", context)

def product(request, product, shop):
    product_detail = Product.objects.get(slug=product)
    context = {'product': product_detail}
    return render(request,"pages/productDetail.html", context)