from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=30, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        string = str(self.user) + "'s cart"
        return string

class Order(models.Model):
    STATUS_CHOICES = [
        ('In process of making', 'IPM'),
        ('In stock', 'INS'),
        ('In delivery', 'IND'),
        ('In your post office', 'IPO')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    address = models.CharField(max_length=100, null=False)
    full_price = models.IntegerField(null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_delivered = models.DateTimeField(null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='IPM')
    delivered = models.BooleanField(default=False)

    def __str__(self):
        string = str(self.user) + "'s order created at " + str(self.date_created)
        return string

    
