# 🧾 Django Sales & Inventory Management System  Database Design
A complete Sales & Inventory Management backend built with **Django ORM**, designed for small to mid-scale businesses.  
This system manages **users, products, categories, customers, invoices, and invoice products**, ensuring accurate stock tracking, billing, and reporting.

---

## 🚀 Features

### 👤 User Management
- User registration & authentication  
- Unique username and email  
- OTP support  
- Related access to categories, products, customers, invoices, & invoice products  

### 🗂 Product & Category Management
- Create and manage categories  
- Add products with pricing, units, and categories  
- Each product and category linked to a specific user  

### 👥 Customer Management
- Store customer details  
- Linked to a user for multi-tenant environments  

### 🧾 Invoice System
- Invoice creation with total, discount, VAT, payment, and due amount  
- Each invoice is assigned to a customer and user  
- Line-item invoice products support  

### 🛒 Invoice Product Items
- Add multiple products to an invoice  
- Accurate quantity and sale price  
- Linked to user, product, invoice, and customer  

---

## 🛠 Technology Stack
- **Python 3.12.3  
- **Django 6 
- **SQLite**  
- **Django ORM**  

---

## 📦 Database Schema (Models Overview)

### **User**
Holds the main user information.  
```python
class User(User.Model):
    username = User.CharField(max_length=150, unique=True)
    email = User.EmailField(unique=True)
    mobile = User.CharField()
    password = User.CharField(max_length=500)
    first_name = User.CharField(max_length=50)
    last_name = User.CharField(max_length=50)
    otp = User.IntegerField()
    created_at = User.DateTimeField(auto_now_add=True)
    updated_at = User.DateTimeField(auto_now=True)
```

### **Category**
Each category belongs to a user.  
```python
class Category(models.Model):
    name = models.CharField(max_length=100)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### **Product**
Stores product information with price and unit.  
```python
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=100)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
### **Customer**
Basic customer information.  
```python
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField()
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
### **Invoice**
Stores overall invoice financial summary.  
```python
class Invoice(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.DecimalField(max_digits=10, decimal_places=2)
    payment = models.DecimalField(max_digits=10, decimal_places=2)
    payment_due = models.DecimalField(max_digits=10, decimal_places=2)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invoices')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='invoices')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
### **InvoiceProduct**
Line items for invoices.  
```python
class InvoiceProduct(models.Model):
    qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invoice_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='invoice_products')
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='invoice_products')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='invoice_products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
Here’s your **Getting Started** section formatted for direct copy-paste as a clean one-page block:

## ▶️ Database Output Diagram 
![Database Diagram](https://raw.githubusercontent.com/mostafaraihan/Django-Sales-Inventory-Database-Design-Project/master/output.png)

## ▶️ Getting Started

### 1. Clone the Repository
```
gh repo clone mostafaraihan/Django-Sales-Inventory-Database-Design-Project
cd Django-Sales-Inventory-Database-Design-Project
````

### 2. Create Virtual Environment

```
python -m venv venv
```
# Linux / Mac
```
source venv/bin/activate
```
# Windows
```
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Apply Migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 5. Run Server

```
python manage.py runserver
```



This is a **ready-to-use, one-page section** for your README.md.  

If you want, I can also make it **even shorter with numbered steps in one code block** for ultra-compact display. Do you want me to do that?
```
