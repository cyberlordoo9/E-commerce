from django.shortcuts import redirect, render

# Create your views here.

from django.contrib import messages
from .models import Order, OrderItem
from .forms import OrderCreateForm, OrderItemForm


def create_order(request):
    if request.method == 'POST':
        order_form = OrderCreateForm(request.POST)
        if order_form.is_valid():
            order = order_form.save()
            messages.success(request, f"Order #{order.order_number} created successfully!")
            return redirect('order_detail', pk=order.pk)
    else:
        order_form = OrderCreateForm()
    return render(request, 'orders/order_form.html', {'form': order_form})
