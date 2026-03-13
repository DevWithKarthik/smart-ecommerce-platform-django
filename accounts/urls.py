from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.customer_login, name="login"),
    path("seller-login/", views.seller_login, name="seller_login"),
    path("delivery-login/", views.delivery_login, name="delivery_login"),
    path("logout/", views.logout_user, name="logout"),
    path("signup/", views.customer_signup, name="customer_signup"),
    path("seller-signup/", views.seller_signup, name="seller_signup"),
    path("delivery-signup/", views.delivery_signup, name="delivery_signup"),
    path("seller-dashboard/", views.seller_dashboard, name="seller_dashboard"),
    path("delivery-dashboard/", views.delivery_dashboard, name="delivery_dashboard"),
]

