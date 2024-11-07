from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Product,Offer,Category

def index(request):
    # Filter products with offers and new arrivals
    offers = Product.objects.filter(has_offer=True)
    arrivels = Product.objects.filter(new_arrivals=True)

    return render(request, "web/index.html", {
        'offers': offers,
        'arrivels': arrivels,
    })


def about(request):
    return render(request,"web/about-us.html")


def product(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)


    return render(request, 'web/product.html', {
        'category': category,
        'categories': categories,
        'products': products,
    })


def contact(request):
    return render(request,"web/contact-us.html")


def offer(request):
    offers = Offer.objects.all()  
    context = {
        'offers': offers, 
    }
    return render(request, "web/offer.html", context)


def categories_view(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'web/category', context)