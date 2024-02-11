# Warehouse Django Site

### 🎯Purpose

Develop a website for a warehouse facility to simplify the accounting of suppliers, customers, and merchandise.

---

### 📝Description

**The project implements the following functionality:**  
1) Registration, authorization, authentication, exit from the account, as well as the user's personal cabinet;  
2) Main page with the ability to navigate through all other pages;  
3) Ability to view (as a table), delete, add, paginate, filter and search for each entity;  
4) Entities: Commodity, Service, Buyer, Seller, Commodity Expense, Commodity Arrival;  
5) The ability to view the report on all expenditures and receipts of goods (separately on different pages), as well as filtering reports by date (per month, per year, per day);  

---

### 🛠️Stack

**Languages**: Python, JavaScript;  
**Framework**: Django;  
**Libraries**: django-datatatable, django-grappelli, django-phonenumber-field, psycopg2-binary, phonenumberslite, python-dotenv;  
**Database**: PostgreSQL;
**Tools**: Docker, docker-compose.

---

### ⚙️Installation

---

1) **Clone the repository**: ```git clone https://github.com/shoksdev/warehouse_work.git```  
2) **Start the project with superuser creation**: ```docker-compose run django python manage.py createsuperuser```  
3) **Bring the project**: ```docker-compose up```

---

### 📙Guidelines for use

1) Go to http://127.0.0.1:8000/expenses/, where you can view all product costs, add/remove a row in the table, change the pagination in the table, search for something;  
2) Go to http://127.0.0.1:8000/customers/, you can view all customers, add/remove a customer, change pagination in the table, search for something, filter records using the buttons in the table columns;  
3) Go to http://127.0.0.1:8000/suppliers/, you can view all sellers, add/remove a seller, change pagination in the table, find something by searching, filter records by using the buttons in the table columns;  
4) Go to http://127.0.0.1:8000/products/ page, where you can view all products, add/remove product, change pagination in the table, find something by searching, filter records by using the buttons in the table columns;  
5) Go to http://127.0.0.1:8000/services/, you can view all services, add/remove a service, change pagination in the table, search for something, filter records using the buttons in the table columns;  
6) Go to http://127.0.0.1:8000/expense_reports/ page, where you can view the expense report, change pagination in the table, search for something using search, filter records using the buttons in the table columns and filter records by date added using the corresponding buttons;  
7) Go to http://127.0.0.1:8000/arrival_reports/, where you can view the parish report, change the pagination in the table, find something using search, filter records using the buttons in the table columns and filter records by date added using the corresponding buttons;  
8) Go to http://127.0.0.1:8000/accounts/register/ to register;  
9) Go to http://127.0.0.1:8000/accounts/login/ to log in to your account;  
10) Go to http://127.0.0.1:8000/accounts/logout/ to log out of the account;  

---

#### Thank you very much for taking the time to share this repository and my profile in general. All the best!
