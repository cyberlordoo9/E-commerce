from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from products.models import ProductVariant, Product
from .models import Cart, CartItem, Wishlist, WishlistItem
from users.models import UserProfile


def cart_detail(request):
    """View all items in the user's cart"""
    user = UserProfile.objects.first()  # Temporary placeholder (replace with request.user)
    cart, created = Cart.objects.get_or_create(user=user)
    items = cart.items.select_related('product_variant')
    total = sum(item.price * item.quantity for item in items)
    return render(request, 'cart/cart_detail.html', {'cart': cart, 'items': items, 'total': total})


def add_to_cart(request, variant_id):
    """Add product variant to cart"""
    user = UserProfile.objects.first()  # Replace with request.user later
    product_variant = get_object_or_404(ProductVariant, id=variant_id)
    cart, created = Cart.objects.get_or_create(user=user)

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product_variant=product_variant,
        defaults={'price': product_variant.price, 'quantity': 1}
    )

    if not created:
        item.quantity += 1
        item.save()

    messages.success(request, f"{product_variant.name} added to your cart.")
    return redirect('cart_detail')


def remove_from_cart(request, item_id):
    """Remove item from cart"""
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    messages.info(request, "Item removed from cart.")
    return redirect('cart_detail')


# Create your views here.
