from django.db import models
from accounts.models import User


# ===============================
# CATEGORY
# ===============================
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# ===============================
# PRODUCT
# ===============================
class Product(models.Model):
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'SELLER'}
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ===============================
# ATTRIBUTE (Size, Color, RAM...)
# ===============================
class ProductAttribute(models.Model):
    name = models.CharField(max_length=100)  # Size, Color, RAM, Storage

    def __str__(self):
        return self.name


# ===============================
# ATTRIBUTE VALUE (M, Red, 8GB...)
# ===============================
class ProductAttributeValue(models.Model):
    attribute = models.ForeignKey(
        ProductAttribute,
        on_delete=models.CASCADE,
        related_name='values'
    )

    value = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.attribute.name} - {self.value}"


# ===============================
# PRODUCT VARIANT
# ===============================
class ProductVariant(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="variants"
    )

    attributes = models.ManyToManyField(ProductAttributeValue)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} Variant"

