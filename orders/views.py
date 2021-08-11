from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CreateOrderForm
from products.models import Product
from .models import Order


@login_required(login_url='accounts:login')
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


@login_required(login_url='accounts:login')
def delete_order(request, *args, **kwargs):
    Order.objects.get(pk=kwargs['pk']).delete()
    return redirect('orders:list')


@login_required(login_url='accounts:login')
def order_list(request):
    order_list = Order.objects.filter(user=request.user)
    return render(request, "orders/order_list.html", {"order_list": order_list})


@login_required(login_url='accounts:login')
def order_detail(request, *args, **kwargs):
    order = Order.objects.get(pk=kwargs['pk'])
    return render(request, "orders/order_detail.html", {"order": order})
