from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from orders.models import Order


def delivery_required(view_func):
    def wrapper(request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect("login")

        if request.user.role != "DELIVERY":
            return redirect("home")   

        return view_func(request, *args, **kwargs)

    return wrapper


@login_required
@delivery_required
def dashboard(request):

    orders = Order.objects.filter(
        delivery_partner=request.user
    ).order_by("-created_at")

    return render(request, "delivery/dashboard.html", {
        "orders": orders
    })


# @login_required
# @delivery_required
# def update_status(request, order_id):

#     order = get_object_or_404(
#         Order,
#         id=order_id,
#         delivery_partner=request.user
#     )

#     if order.status == "PENDING":
#         order.status = "SHIPPED"

#     elif order.status == "SHIPPED":
#         order.status = "OUT_FOR_DELIVERY"   

#     elif order.status == "OUT_FOR_DELIVERY":
#         order.status = "DELIVERED"

#     order.save()

#     return redirect("delivery:dashboard")

# MARK PICKED
@login_required
def mark_picked(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        delivery_partner=request.user
    )

    order.status = "OUT_FOR_DELIVERY"
    order.save()

    return redirect("delivery:dashboard")


# MARK DELIVERED
@login_required
def mark_delivered(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        delivery_partner=request.user
    )

    order.status = "DELIVERED"
    order.save()

    return redirect("delivery:dashboard")