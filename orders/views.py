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
        quantity = form.cleaned_data.get('quantity')
        Order.objects.create(
            user=user,
            products=products,
            address=address,
            quantity=quantity,
            total_price=quantity*product.price)
        return redirect('orders:list')
    context = {
        "form": form,
        "product": product,
    }
    return render(request, "orders/create_order.html", context)


def delete_order(request, *args, **kwargs):
    order = Order.objects.get(pk=kwargs['pk'])
    if request.method == "POST":
        order.delete()
        return redirect('orders:list')
    return render(request, "orders/delete_order.html", {"order": order})


def order_list(request):
    order_list = Order.objects.filter(user=request.user)
    return render(request, "orders/order_list.html", {"order_list": order_list})


def order_detail(request, *args, **kwargs):
    order = Order.objects.get(pk=kwargs['pk'])
    return render(request, "orders/order_detail.html", {"order": order})
