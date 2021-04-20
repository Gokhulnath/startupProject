from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 
from . import views
urlpatterns =[
    path('',views.index, name='index'),
    path('index/',views.index, name='index'),
    path('product/',views.product, name='product'),
    path('shop/',views.shop, name='shop'),
    path('shoplist/',views.shoplist, name='shoplist'),
    path('cart/',views.cart, name='cart'),
    path('shopProducts/',views.shopProducts, name='shopProducts'),
    path('faq/',views.faq, name='faq'),
    path('contact/',views.contact, name='contact'),
    path('checkout/',views.checkout, name='checkout'),
    path('blog/',views.blog, name='blog'),
    path('post/',views.post, name='post'),
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
