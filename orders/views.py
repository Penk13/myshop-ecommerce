from django.shortcuts import render, redirect

from .forms import CreateOrderForm
from products.models import Product
from .models import Order


def create_order(request, *args, **kwargs):
    product = Product.objects.get(pk=kwargs['pk'])
    form = CreateOrderForm(request.POST or None)
    if form.is_valid():
        user = request.user
        products = product
        address = form.cleaned_data.get('address')
        total_price = product.price
        Order.objects.create(
            user=user,
            products=products,
            address=address,
            total_price=total_price)
        return redirect('homepage')
    context = {
        "form": form,
        "product": product,
    }
    return render(request, "orders/create_order.html", context)


def delete_order(request):
    pass


def order_list(request):
    order_list = Order.objects.filter(user=request.user)
    return render(request, "orders/order_list.html", {"order_list": order_list})
