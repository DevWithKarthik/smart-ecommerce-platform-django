from django.urls import path
from . import views
from .views import add_to_cart, cart_detail, remove_from_cart

app_name = "cart"

urlpatterns = [
    path("add/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path("", cart_detail, name="cart_detail"),
    path("remove/<int:variant_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("increase/<int:variant_id>/", views.increase_quantity, name="increase_quantity"),
    path("decrease/<int:variant_id>/", views.decrease_quantity, name="decrease_quantity"),
]
