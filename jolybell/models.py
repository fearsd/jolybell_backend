from django.db import models

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
    