from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import CategorySerializer, ProductListSerializer, ProductDetailSerializer
from .models import Category, Product, Cart

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

def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    categories = Category.objects.all()
    context = {'categories': categories, 'product': product}
    return render(request, 'jolybell/product.html', context)

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart, l = Cart.objects.get_or_create(user=request.user)
    cart.products.add(product)
    return redirect(reverse('index'))

def cart(request):
    user = request.user
    cart = get_object_or_404(Cart, user=user)
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {'categories': categories, 'user': user, 'products': cart.products.all()}
        return render(request, 'jolybell/cart.html', context)
    else:
        pass

        
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
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, pk):
    try:
        product = get_object_or_404(Product, pk=pk)
    except:
        return JsonResponse({"status": 404})
    if request.method == 'GET':
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)