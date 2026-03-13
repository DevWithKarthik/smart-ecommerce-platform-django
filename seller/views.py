from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Sum
from django.utils import timezone
from datetime import datetime
from prodcuts.models import Product, ProductVariant
from orders.models import OrderItem
from .forms import SellerProductForm, ProductVariantForm
from django.contrib import messages


# -------------------------------
# Seller Role Protection
# -------------------------------
def seller_required(view_func):
    def wrapper(request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect("login")

        if request.user.role != "SELLER":
            return redirect("home")

        return view_func(request, *args, **kwargs)

    return wrapper


# -------------------------------
# 1️⃣ DASHBOARD
# -------------------------------
@login_required
@seller_required
def dashboard(request):

    products = Product.objects.filter(seller=request.user)

    order_items = OrderItem.objects.filter(
        variant__product__seller=request.user
    )

    total_products = products.count()
    total_orders = order_items.count()
    pending_orders = order_items.filter(order__status="PENDING").count()

    total_revenue = sum(
        item.price * item.quantity for item in order_items
    )

    context = {
        "total_products": total_products,
        "total_orders": total_orders,
        "pending_orders": pending_orders,
        "total_revenue": total_revenue,
    }

    return render(request, "seller/dashboard.html", context)


# -------------------------------
# 2️⃣ MY PRODUCTS
# -------------------------------
@login_required
@seller_required
def products(request):
    seller_products = Product.objects.filter(seller=request.user)

    return render(request, "seller/products.html", {
        "products": seller_products
    })


# -------------------------------
# ADD PRODUCTS
# -------------------------------
@login_required
@seller_required
def add_product(request):

    if request.method == "POST":
        form = SellerProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user  # 🔥 important
            product.save()

            return redirect("seller:products")

    else:
        form = SellerProductForm()

    return render(request, "seller/add_product.html", {
        "form": form
    })
    
# -------------------------------
# Edit PRODUCTS
# -------------------------------

@login_required
@seller_required
def edit_product(request, pk):

    product = get_object_or_404(Product, pk=pk, seller=request.user)

    if request.method == "POST":
        form = SellerProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("seller:products")
    else:
        form = SellerProductForm(instance=product)

    return render(request, "seller/add_product.html", {
        "form": form
    })

# -------------------------------
# DELETE PRODUCTS
# -------------------------------

@login_required
@seller_required
def delete_product(request, pk):

    product = get_object_or_404(Product, pk=pk, seller=request.user) # ensure seller can only delete their own products
    product.delete()

    return redirect("seller:products")


# -------------------------------
# 3️⃣ ORDERS
# -------------------------------
@login_required
@seller_required
def orders(request):

    seller_orders = OrderItem.objects.filter(
        variant__product__seller=request.user
    ).select_related("order", "variant__product")

    return render(request, "seller/orders.html", {
        "order_items": seller_orders
    })


# -------------------------------
# 4️⃣ EARNINGS
# -------------------------------
@login_required
@seller_required
def earnings(request):

    order_items = OrderItem.objects.filter(
        variant__product__seller=request.user
    )

    # Total earnings
    total_earnings = sum(
        item.price * item.quantity for item in order_items
    )

    # This month's earnings
    now = timezone.now()
    current_month = order_items.filter(
        order__created_at__year=now.year,
        order__created_at__month=now.month
    )

    monthly_earnings = sum(
        item.price * item.quantity for item in current_month
    )

    return render(request, "seller/earnings.html", {
        "total_earnings": total_earnings,
        "monthly_earnings": monthly_earnings
    })
    
# Manage Variants on Products

@login_required
@seller_required
def manage_variants(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id,
        seller=request.user
    )

    variants = product.variants.all()

    if request.method == "POST":
        form = ProductVariantForm(request.POST)

        if form.is_valid():
            selected_attributes = form.cleaned_data["attributes"]

            # Check for duplicate
            for existing in product.variants.all():
                if set(existing.attributes.all()) == set(selected_attributes):
                    messages.error(request, "This variant already exists!")
                    return redirect("seller:manage_variants", product_id=product.id)

            variant = form.save(commit=False)
            variant.product = product
            variant.save()
            form.save_m2m()

            return redirect("seller:manage_variants", product_id=product.id)
    else:
        form = ProductVariantForm()

    return render(request, "seller/manage_variants.html", {
        "product": product,
        "variants": variants,
        "form": form
    })
    
# Edit Product Variants 

@login_required
@seller_required
def edit_variant(request, variant_id):

    variant = get_object_or_404(
        ProductVariant,
        id=variant_id,
        product__seller=request.user
    )

    if request.method == "POST":
        form = ProductVariantForm(request.POST, instance=variant)

        if form.is_valid():
            form.save()
            return redirect(
                "seller:manage_variants",
                product_id=variant.product.id
            )
    else:
        form = ProductVariantForm(instance=variant)

    return render(request, "seller/edit_variant.html", {
        "form": form,
        "variant": variant
    })


@login_required
@seller_required
def delete_variant(request, variant_id):

    variant = get_object_or_404(
        ProductVariant,
        id=variant_id,
        product__seller=request.user
    )

    product_id = variant.product.id
    variant.delete()

    return redirect("seller:manage_variants",
                    product_id=product_id)