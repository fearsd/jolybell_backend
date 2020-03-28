from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Category

def index(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'jolybell/index.html', context)

def category(request, name):
    category = get_object_or_404(Category, name=name)
    categories = Category.objects.all()
    context = {'category': category, 'categories': categories}
    return render(request, 'jolybell/category.html', context)
