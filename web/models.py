
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    subname = models.CharField(max_length=200)
    image = models.ImageField(upload_to='product_images/')
    image1 = models.ImageField(upload_to='product_images/')
    price = models.IntegerField()
    gram = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    has_offer = models.BooleanField(default=False)
    new_arrivals = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
        
    

class Offer(models.Model):
    name = models.CharField(max_length=200)
    subname = models.CharField(max_length=200)
    image = models.ImageField(upload_to='offer_images/')
    image1 = models.ImageField(upload_to='offer_images/')
    price = models.IntegerField()
    gram=models.IntegerField()

    class Meta:
        verbose_name = ('Offer')
        verbose_name_plural = ("Offer")

    def __str__(self):
        return self.name
    

