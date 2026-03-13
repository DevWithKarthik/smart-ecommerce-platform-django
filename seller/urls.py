from django.urls import path
from . import views

app_name = "seller"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("products/", views.products, name="products"),
    path("orders/", views.orders, name="orders"),
    path("earnings/", views.earnings, name="earnings"),
    path("add-product/", views.add_product, name="add_product"),
    path("edit-product/<int:pk>/", views.edit_product, name="edit_product"),
    path("delete-product/<int:pk>/", views.delete_product, name="delete_product"),
    path("variants/<int:product_id>/", views.manage_variants, name="manage_variants"),
    path("edit-variant/<int:variant_id>/", views.edit_variant, name="edit_variant"),
    path("delete-variant/<int:variant_id>/", views.delete_variant, name="delete_variant"),
]