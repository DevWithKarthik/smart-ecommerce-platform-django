class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("cart")

        if not cart:
            cart = self.session["cart"] = {}

        self.cart = cart

    def add(self, variant, quantity=1):
        variant_id = str(variant.id)

        if variant_id not in self.cart:
            self.cart[variant_id] = {
                "product_name": variant.product.name,
                "price": float(variant.price),
                "quantity": 0,
                "image": variant.product.image.url if variant.product.image else "",
                "attributes": [
                    f"{attr.attribute.name}: {attr.value}"
                    for attr in variant.attributes.all()
                ]
            }

        self.cart[variant_id]["quantity"] += quantity
        self.save()


    def remove(self, variant_id):
        variant_id = str(variant_id)

        if variant_id in self.cart:
            del self.cart[variant_id]
            self.save()

    def save(self):
        self.session.modified = True
        
    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True

    def get_items(self):
        items = []

        for variant_id, item in self.cart.items():
            item_copy = item.copy()
            item_copy["total_price"] = item["price"] * item["quantity"]
            items.append((variant_id, item_copy))

        return items

    def get_total_price(self):
        return sum(
            item["price"] * item["quantity"]
            for item in self.cart.values()
        )
        
    def increase(self, variant_id):
        variant_id = str(variant_id)

        if variant_id in self.cart:
            self.cart[variant_id]["quantity"] += 1
            self.save()


    def decrease(self, variant_id):
        variant_id = str(variant_id)

        if variant_id in self.cart:
            self.cart[variant_id]["quantity"] -= 1

            if self.cart[variant_id]["quantity"] <= 0:
                del self.cart[variant_id]

            self.save()

