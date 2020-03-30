from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *
from .models import Category, Product, Cart, Order

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
        address = request.POST['address']
        full_price = 0
        for product in cart.products.all():
            full_price += product.price

        order = Order(user=user, address=address, full_price=full_price)
        order.save()
        for product in cart.products.all():
            order.products.add(product)
        for product in cart.products.all():
            product.cart_set.clear()
        cart.products.clear()
        return redirect(reverse('index'))

def user_cabinet(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    categories = Category.objects.all()
    context = {'categories': categories, 'user': user , 'orders': orders}
    return render(request, 'jolybell/cabinet.html', context)

def order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    categories = Category.objects.all()
    context = {'categories': categories, 'order': order}
    return render(request, 'jolybell/order.html', context)
        

        
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

@api_view(['GET'])
def cart_collection(request):
    if request.method == 'GET':
        carts = Cart.objects.all()
        serializer = CartListSerializer(carts, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def cart_detail(request, pk):
    try:
        cart = get_object_or_404(Cart, pk=pk)
    except:
        return JsonResponse({'status': 404})
    if request.method == 'GET':
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    else:
        pr_pk = request.data.get('product')
        product = get_object_or_404(Product, pk=pr_pk)
        cart.products.add(product)
        return JsonResponse({'status': 'ok'})



@api_view(['GET'])
def order_collection(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def order_detail(request, pk):
    try:
        order = get_object_or_404(Order, pk=pk)
    except:
        return JsonResponse({'status': 404})
    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)
