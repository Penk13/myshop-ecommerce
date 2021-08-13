from django.shortcuts import render, get_object_or_404

from .models import Product, Category


# Views for base.html
def navbar(request):
    # Get all category from Category Table
    category_list = Category.objects.all()
    return {'category_list': category_list}


def homepage(request):
    product_list = []
    # Get all available product
    for product in Product.objects.all():
        if product.available():
            product_list.append(product)
    context = {'product_list': product_list}
    return render(request, 'products/homepage.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)
