from django.contrib import admin
from .models import Product, Offer, Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')  
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ("name",)
