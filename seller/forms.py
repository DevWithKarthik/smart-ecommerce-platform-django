from django import forms
from prodcuts.models import Product
from prodcuts.models import ProductVariant, ProductAttributeValue



class SellerProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            "category",
            "name",
            "description",
            "base_price",
            "image",
            "is_active",
        ]
        
class ProductVariantForm(forms.ModelForm):

    attributes = forms.ModelMultipleChoiceField(
        queryset=ProductAttributeValue.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = ProductVariant
        fields = ["attributes", "price", "stock"]
        
        
        