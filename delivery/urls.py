from django.urls import path
from . import views

app_name = "delivery"

urlpatterns = [

    path("dashboard/", views.dashboard, name="dashboard"),

    path(
        "picked/<int:order_id>/",
        views.mark_picked,
        name="mark_picked"
    ),

    path(
        "delivered/<int:order_id>/",
        views.mark_delivered,
        name="mark_delivered"
    ),

]