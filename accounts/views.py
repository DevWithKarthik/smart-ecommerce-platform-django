from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import DeliveryProfile, SellerProfile, User


@login_required
def seller_dashboard(request):
    if request.user.role != "SELLER":
        raise PermissionDenied
    return render(request, "seller/dashboard.html")


@login_required
def delivery_dashboard(request):
    if request.user.role != "DELIVERY":
        raise PermissionDenied
    return render(request, "delivery/dashboard.html")


def role_login(request, expected_role):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:

            # Check role
            if user.role != expected_role:
                messages.error(request, "You are not authorized for this login.")
                return redirect(request.path)

            # Check approval (only for seller & delivery)
            if user.role in ["SELLER", "DELIVERY"] and not user.is_approved:
                messages.error(request, "Your account is waiting for admin approval.")
                return redirect(request.path)

            login(request, user)

            if user.role == "CUSTOMER":
                return redirect("home")

            elif user.role == "SELLER":
                return redirect("seller:dashboard")

            elif user.role == "DELIVERY":
                return redirect("delivery:dashboard")

        else:
            messages.error(request, "Invalid credentials.")

    return render(request, "accounts/login.html", {"role": expected_role})


def customer_login(request):
    return role_login(request, "CUSTOMER")


def seller_login(request):
    return role_login(request, "SELLER")


def delivery_login(request):
    return role_login(request, "DELIVERY")

def logout_user(request):
    logout(request)
    return redirect("home")

def customer_signup(request):

    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            role="CUSTOMER",
            is_approved=True
        )

        login(request, user)

        return redirect("home")

    return render(request, "accounts/customer_signup.html")

def seller_signup(request):

    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        business_name = request.POST["business_name"]
        gst_number = request.POST["gst_number"]
        address = request.POST["address"]

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            role="SELLER",
            is_approved=False
        )

        SellerProfile.objects.create(
            user=user,
            business_name=business_name,
            gst_number=gst_number,
            address=address
        )

        return render(request, "accounts/waiting_approval.html")

    return render(request, "accounts/seller_signup.html")


def delivery_signup(request):

    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        hub_name = request.POST["hub_name"]
        hub_area_sqft = request.POST["hub_area"]
        employees_count = request.POST["employees"]

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            role="DELIVERY",
            is_approved=False
        )

        DeliveryProfile.objects.create(
            user=user,
            hub_name=hub_name,
            hub_area_sqft=hub_area_sqft,
            employees_count=employees_count
        )

        return render(request, "accounts/waiting_approval.html")

    return render(request, "accounts/delivery_signup.html")