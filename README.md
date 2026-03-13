# Smart E-Commerce Platform – Role-Based Marketplace System

A full-stack Django e-commerce application designed with a **role-based architecture** that supports **Customers, Sellers, and Delivery Partners**.
The platform enables product management, order processing, delivery tracking, and session-based shopping cart functionality.

This project demonstrates real-world **backend architecture, database design, and scalable e-commerce workflows**.

---

# 🚀 Features

### Customer Module

* User registration and authentication
* Browse products with dynamic variants
* Add products to cart (session-based cart)
* Checkout and place orders
* Track order status

### Seller Module

* Seller registration with admin approval
* Seller dashboard
* Add / edit / delete products
* Manage product variants (Color, Size, RAM, Storage)
* View and process orders

### Delivery Partner Module

* Delivery partner registration with admin approval
* Delivery dashboard optimized for mobile usage
* View assigned deliveries
* Mark orders as **Picked**, **Out for Delivery**, and **Delivered**

### Order Management

* Order creation from cart
* Seller order tracking
* Delivery partner assignment
* Status updates across modules

### Product Variant System

Dynamic product attribute system supporting:

* Color
* Size
* RAM
* Storage
* Any future attribute without schema change

### Shopping Cart

* Session-based cart
* Quantity management
* Automatic total calculation
* Variant-specific cart items

---

# 🧠 Architecture

The system follows a **modular Django architecture** with separate apps for different roles.

```
smart_ecommerce/
│
├── accounts/        # Custom user model & authentication
├── products/        # Product catalog & variants
├── cart/            # Session based shopping cart
├── orders/          # Order processing
├── seller/          # Seller dashboard & product management
├── delivery/        # Delivery partner dashboard
├── customers/       # Customer frontend pages
│
├── static/
├── templates/
└── manage.py
```

---

# 🗄️ Database Design

Core models include:

* User (Custom AbstractUser with role)
* Category
* Product
* ProductVariant
* ProductAttribute
* ProductAttributeValue
* Order
* OrderItem

This design supports **dynamic variant combinations** for different product categories.

Example:

```
Mobile
  ├── Color
  └── Storage

Fashion
  ├── Color
  └── Size
```

---

# 🔐 Role-Based Authentication

Users are assigned roles:

* CUSTOMER
* SELLER
* DELIVERY
* ADMIN

Access to dashboards and features is restricted using:

* Django authentication
* Custom role decorators
* Login redirection logic

Example login flow:

```
User Login
   ↓
Role Verification
   ↓
Redirect to Role Dashboard
```

---

# 📦 Order Workflow

Customer → Seller → Delivery Partner

```
Customer places order
        ↓
Seller receives order
        ↓
Seller processes order
        ↓
Delivery partner picks order
        ↓
Order delivered to customer
```

Order statuses:

* Pending
* Confirmed
* Shipped
* Out for Delivery
* Delivered
* Cancelled

---

# 🛠️ Technologies Used

Backend

* Python
* Django
* Django ORM

Frontend

* HTML
* CSS
* Bootstrap

Database

* MySQL

Other

* Django Sessions
* Django Signals
* Role-based access control

---

# ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/smart-ecommerce-platform.git
cd smart-ecommerce-platform
```

### 2️⃣ Create virtual environment

```
python -m venv venv
```

Activate environment:

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

Create `.env` file:

```
DB_NAME=your_db
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
```

### 5️⃣ Apply migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create superuser

```
python manage.py createsuperuser
```

### 7️⃣ Run development server

```
python manage.py runserver
```

---

# 📊 Key Concepts Demonstrated

* Django role-based authentication
* Dynamic product variant architecture
* Session-based shopping cart
* Multi-module dashboard system
* Efficient ORM usage (`select_related`, `prefetch_related`)
* Order processing workflow
* Clean modular Django project structure

---

# 📌 Future Improvements

* Payment gateway integration (Stripe / Razorpay)
* Real-time order tracking
* Push notifications
* Product search & filtering
* AI-based product recommendation system

---

# 👨‍💻 Author

**Karthik M**

Python Full-Stack Developer | Django Developer
