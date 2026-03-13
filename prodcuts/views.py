from django.shortcuts import render, get_object_or_404
from .models import Product, ProductVariant


# ==========================
# PRODUCT LIST
# ==========================
def product_list(request):
    products = Product.objects.filter(is_active=True)

    return render(request, "customers/product_list.html", {
        "products": products
    })


# ==========================
# PRODUCT DETAIL
# ==========================
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, is_active=True)

    variants = product.variants.prefetch_related("attributes__attribute")

    attributes = {}

    for variant in variants:
        for attr_value in variant.attributes.all():
            attr_name = attr_value.attribute.name

            if attr_name not in attributes:
                attributes[attr_name] = set()

            attributes[attr_name].add(attr_value)

    total_stock = sum(v.stock for v in variants)

    context = {
        "product": product,
        "variants": variants,
        "attributes": attributes,
        "total_stock": total_stock,
    }

    return render(request, "customers/product_details.html", context)

