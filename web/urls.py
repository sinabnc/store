from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
     path("",views.index,name="index"),
     path("about/",views.about,name="about"),
     path("product/",views.product,name="product"),
     path("offer/",views.offer,name="offer"),
     path("contact/",views.contact,name="contact"),
     path('products/category/<slug:category_slug>/', views.product, name='product_list_by_category'),

]
