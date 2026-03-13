from django.contrib import admin
from .models import (
    Category,
    Product,
    ProductAttribute,
    ProductAttributeValue,
    ProductVariant
)


# ================= CATEGORY =================
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'is_active')


# ================= PRODUCT =================
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'base_price', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('name',)


# ================= ATTRIBUTE =================
@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('name',)


# ================= ATTRIBUTE VALUE =================
@admin.register(ProductAttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    list_display = ('attribute', 'value')
    list_filter = ('attribute',)


# ================= VARIANT =================
@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'stock')
    list_filter = ('product',)
    filter_horizontal = ('attributes',)
