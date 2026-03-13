from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .models import Order, OrderItem


@login_required
def checkout(request):

    cart = Cart(request)

    if not cart.get_items():
        return redirect("cart:cart_detail")

    if request.method == "POST":

        full_name = request.POST.get("full_name")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        pincode = request.POST.get("pincode")

        order = Order.objects.create(
            user=request.user,
            full_name=full_name,
            phone=phone,
            address=address,
            city=city,
            state=state,
            pincode=pincode,
            total_amount=cart.get_total_price(),
        )

        for variant_id, item in cart.get_items():
            OrderItem.objects.create(
                order=order,
                variant_id=variant_id,
                quantity=item["quantity"],
                price=item["price"],
            )

        cart.clear()

        return redirect("orders:order_success", order_id=order.id)

    return render(request, "customers/checkout.html", {
        "cart_items": cart.get_items(),
        "total": cart.get_total_price(),
    })


@login_required
def order_success(request, order_id):
    return render(request, "customers/order_success.html", {
        "order_id": order_id
    })