from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product

def index(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'jolybell/index.html', context)

def category(request, name):
    category = get_object_or_404(Category, name=name)
    categories = Category.objects.all()
    products = Product.objects.filter(category=category)

    context = {'category': category, 'categories': categories, 'products': products}
    return render(request, 'jolybell/category.html', context)

@api_view(['GET'])
def category_collection(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def products_collection(request, name):
    try:
        category = get_object_or_404(Category, name=name)
    except:
        return JsonResponse({"status": 404})
    if request.method == 'GET':
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)