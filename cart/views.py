from django.shortcuts import render, redirect, get_object_or_404
import cart
from prodcuts.models import Product
from .cart import Cart
from prodcuts.models import ProductVariant, ProductAttributeValue

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    quantity = int(request.POST.get("quantity", 1))

    # Collect selected attribute value IDs
    selected_values = []

    for key, value in request.POST.items():
        if key.startswith("attribute_") and value:
            selected_values.append(int(value))

    # Find matching variant
    variant = None

    for v in product.variants.all():
        variant_values = list(
            v.attributes.values_list("id", flat=True)
        )

        if set(selected_values) == set(variant_values):
            variant = v
            break

    if not variant:
        return redirect("prodcuts:product_detail", pk=product.id)

    # Check stock
    if quantity > variant.stock:
        quantity = variant.stock

    cart = Cart(request)
    cart.add(variant, quantity)

    return redirect("cart:cart_detail")




def cart_detail(request):
    cart = Cart(request)

    return render(request, "customers/cart.html", {
        "cart_items": cart.get_items(),
        "total": cart.get_total_price(),
    })


def remove_from_cart(request, variant_id):
    cart = Cart(request)
    cart.remove(variant_id)

    return redirect("cart:cart_detail")

def increase_quantity(request, variant_id):
    cart = Cart(request)
    cart.increase(variant_id)
    return redirect("cart:cart_detail")


def decrease_quantity(request, variant_id):
    cart = Cart(request)
    cart.decrease(variant_id)
    return redirect("cart:cart_detail")
