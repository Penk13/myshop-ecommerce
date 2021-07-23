from django.shortcuts import render

from .models import Product, Category


# Views for base.html
def navbar(request):
    # Get all category from Category Table
    category_list = Category.objects.all()
    return {'category_list': category_list}


def homepage(request):
    # Get all object from Product Table
    product_list = Product.objects.all()
    context = {'product_list': product_list}
    return render(request, 'products/homepage.html', context)


def product_detail(request, pk):
    # Got one object which id is depends on url
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)
