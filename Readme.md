# 🛍️ ShopKickora

A full-stack **E-Commerce Web Application** built entirely with **Django**, designed to provide a seamless online shopping experience with secure authentication, product management, cart & wishlist functionality, order management, online payments, and a comprehensive admin dashboard.

The application follows a **Server-Side Rendering (SSR)** architecture using Django Templates, delivering fast page loads, improved SEO, and a traditional MVC workflow without a separate frontend framework.

---

## 🚀 Features

### 👤 Customer Features

- User Registration & Login
- OTP Verification
- Browse Products
- Product Search
- Product Filtering
- Category Browsing
- Brand Browsing
- Product Details
- Product Reviews & Ratings
- Wishlist Management
- Shopping Cart
- Coupon Application
- Secure Checkout
- Razorpay Payment Integration
- Cash on Delivery (COD)
- Wallet Payments
- Order Placement
- Order History
- Order Cancellation
- Product Returns
- Wallet Refunds
- Address Management
- User Profile Management
- Password Change
- Secure Logout

### 🛠️ Admin Features

- Secure Admin Login
- Dashboard with Sales Analytics
- Product Management (CRUD)
- Category Management
- Brand Management
- Banner Management
- Offer Management
- Coupon Management
- User Management
- Order Management
- Inventory Management
- Wallet Management
- Sales Reports
- Revenue Analytics

---

## 🏗️ Tech Stack

### 🔹 Backend

- Python
- Django
- PostgreSQL
- Razorpay API
- Cloudinary

### 🔹 Frontend (Server-Side Rendered)

- Django Templates
- HTML5
- CSS3
- Bootstrap
- JavaScript

### 🔹 Database

- PostgreSQL

### 🔹 Third-Party Services

- Razorpay Payment Gateway
- Cloudinary Image Storage

---

## 🔐 Authentication & Authorization

- Django Authentication System
- Session-Based Authentication
- OTP Verification
- Role-Based Authorization
- Protected Views
- Secure Password Hashing
- CSRF Protection
- Secure Session Management

---

## 📁 Project Structure

```text
shopkickora/
│
├── accounts/
├── products/
├── cart/
├── orders/
├── payments/
├── wallet/
├── coupons/
├── offers/
├── dashboard/
├── templates/
├── static/
├── media/
├── shopkickora/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 🔹 Clone Repository

```bash
git clone https://github.com/prithvirajpu/shopkickora.git

cd shopkickora
```

---

### 🔹 Create Virtual Environment

```bash
python -m venv venv
```

### 🔹 Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 🔹 Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your_secret_key

DEBUG=True

DATABASE_URL=your_database_url

RAZORPAY_KEY_ID=your_key

RAZORPAY_KEY_SECRET=your_secret

CLOUDINARY_CLOUD_NAME=your_cloud_name

CLOUDINARY_API_KEY=your_api_key

CLOUDINARY_API_SECRET=your_api_secret
```

---

### 🔹 Apply Database Migrations

```bash
python manage.py migrate
```

---

### 🔹 Create Superuser

```bash
python manage.py createsuperuser
```

---

### 🔹 Run Development Server

```bash
python manage.py runserver
```

---

## 🛒 Shopping Workflow

1. User registers or logs in.
2. Browse products by category or brand.
3. Search and filter products.
4. Add products to wishlist or cart.
5. Apply available coupons.
6. Proceed to checkout.
7. Select payment method:
   - Razorpay
   - Cash on Delivery
   - Wallet
8. Complete payment.
9. Order is successfully placed.
10. User tracks order status.
11. Eligible cancellations and returns are refunded to the wallet.

---

## 💳 Payment Workflow

1. User proceeds to checkout.
2. Chooses a payment method.
3. Razorpay securely processes the payment.
4. Payment is verified.
5. Order is confirmed.
6. Inventory is updated.
7. Wallet transactions are recorded for refunds and wallet payments.

---

## 📦 Order Status Workflow

```text
Pending
   │
   ▼
Confirmed
   │
   ▼
Packed
   │
   ▼
Shipped
   │
   ▼
Out For Delivery
   │
   ▼
Delivered
```

Additional Statuses

- Cancelled
- Returned
- Refunded

---

## 🛡️ Security Features

- Django Authentication
- Session-Based Login
- OTP Verification
- Secure Password Hashing
- CSRF Protection
- SQL Injection Protection
- XSS Protection
- Input Validation
- Role-Based Access Control
- Secure Payment Verification

---

## 📊 Admin Dashboard Features

- Sales Dashboard
- Revenue Reports
- Order Analytics
- Product Management
- Inventory Monitoring
- Customer Management
- Coupon Management
- Offer Management
- Wallet Monitoring
- Monthly Sales Reports

---

## 🎯 Future Enhancements

- Product Reviews & Ratings
- AI-Based Product Recommendations
- Email Notifications
- Wishlist Sharing
- Advanced Inventory Forecasting
- CI/CD Pipeline
- Elasticsearch Product Search

---

## 👨‍💻 Author

**Prithviraj P U**