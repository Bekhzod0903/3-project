from django.shortcuts import render
from .models import Category, Product
# Create your views here.


def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)

def get_product(request,pk):
    category = Category.objects.get(pk=pk)
    products = Product.objects.filter(category=category)
    context = {
        'products': products
    }
    return render(request, 'products.html', context=context)