from django.contrib import admin
from .models import UserWH, Product, Supplier, Customer, Arrival, Expense


# Регистрируем в админку пользователя
class UserWHAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fields = (('username', 'email'), ('first_name', 'last_name'), ('password',), ('position',), ('is_active',),
              ('is_staff', 'is_superuser'), 'groups', 'user_permissions', ('last_login', 'date_joined'))


admin.site.register(UserWH, UserWHAdmin)


# Регистрируем в админку Товар
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'name', 'category', 'quantity', 'price')


# Регистрируем в админку Продавца
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_id', 'company_name', 'country', 'city', 'address', 'phone', 'website')


# Регистрируем в админку Покупателя
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'first_name', 'last_name', 'country', 'city', 'address', 'phone', 'email')


# Регистрируем в админку Расход
@admin.register(Arrival)
class ArrivalAdmin(admin.ModelAdmin):
    list_display = ('arrival_id', 'supplier_id', 'quantity', 'arrival_date')


# Регистрируем в админку Приход
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('expense_id', 'customer_id', 'quantity', 'expense_date')
