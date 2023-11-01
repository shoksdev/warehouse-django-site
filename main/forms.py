from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserWH, Product, Supplier, Customer, Arrival, Expense


# Форма для регистрации пользователя
class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserWH
        fields = ('username', 'first_name', 'last_name', 'position', 'email', 'password1', 'password2',)


# Форма для создания Товара
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
        'product_id', 'name', 'description', 'sku', 'category', 'quantity', 'price', 'units_in_stock', 'units_on_order',
        'reorder_level', 'discontinued',)


# Форма для создания Продавца
class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'


# Форма для создания Покупателя
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


# Форма для создания Прихода
class ArrivalForm(forms.ModelForm):
    class Meta:
        model = Arrival
        fields = '__all__'
        exclude = ('user',)


# Форма для создания Расхода
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        exclude = ('user',)
