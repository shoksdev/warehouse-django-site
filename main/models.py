from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


# Модель пользователя, наследуем от AbstractUser с добавлением поля "Должность"
class UserWH(AbstractUser):
    position = models.CharField(max_length=50, verbose_name='Должность')

    class Meta:
        app_label = 'main'


# Модель Товара
class Product(models.Model):
    product_id = models.IntegerField(primary_key=True, verbose_name='№ Товара')
    name = models.CharField(max_length=255, verbose_name='Название товара', unique=True)
    description = models.TextField(verbose_name='Описание товара')
    sku = models.CharField(max_length=50, verbose_name='СКУ')
    category = models.CharField(max_length=255, verbose_name='Категория товара')
    quantity = models.IntegerField(default=0, verbose_name='Количество единиц товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    units_in_stock = models.IntegerField(default=0, verbose_name='Единиц на складе')
    units_on_order = models.IntegerField(default=0, verbose_name='Единиц под заказ')
    reorder_level = models.IntegerField(default=0, verbose_name='Уровень заказа')
    discontinued = models.BooleanField(default=False, verbose_name='Снято с производства')

    class Meta:
        ordering = ['product_id']

    def __str__(self):
        return self.name

    # Используется для класса изменения Товара
    def get_absolute_url(self):
        return f'/products/change/{self.product_id}'


# Модель Продавца
class Supplier(models.Model):
    supplier_id = models.IntegerField(primary_key=True, verbose_name='№ Продавца')
    contact_title = models.CharField(max_length=255, verbose_name='Название контакта', unique=True)
    contact_name = models.CharField(max_length=255, verbose_name='Имя контакта')
    company_name = models.CharField(max_length=255, verbose_name='Название компании', unique=True)
    country = models.CharField(max_length=255, verbose_name='Страна', null=True, blank=True)
    region = models.CharField(max_length=255, verbose_name='Регион', null=True, blank=True)
    city = models.CharField(max_length=255, verbose_name='Город', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)
    postal_code = models.CharField(max_length=255, verbose_name='Почтовый индекс', null=True, blank=True)
    phoneNumberRegex = RegexValidator(regex=r'^((\+\d{,4})[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$')
    phone = models.CharField(validators=[phoneNumberRegex], max_length=16, null=True, blank=True, unique=True,
                             verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронная почта')
    website = models.URLField(max_length=255, verbose_name='Веб-сайт')

    class Meta:
        ordering = ['supplier_id']

    def __str__(self):
        return self.company_name

    # Используется для класса изменения Продавца
    def get_absolute_url(self):
        return f'/suppliers/change/{self.supplier_id}'


# Модель Покупателя
class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True, verbose_name='№ Покупателя')
    first_name = models.CharField(max_length=255, verbose_name='Имя покупателя', unique=True)
    last_name = models.CharField(max_length=255, verbose_name='Фамилия покупателя', unique=True)
    country = models.CharField(max_length=255, verbose_name='Страна', null=True, blank=True)
    region = models.CharField(max_length=255, verbose_name='Регион', null=True, blank=True)
    city = models.CharField(max_length=255, verbose_name='Город', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)
    postal_code = models.CharField(max_length=255, verbose_name='Почтовый индекс', null=True, blank=True)
    phoneNumberRegex = RegexValidator(regex=r'^((\+\d{,4})[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$')
    phone = models.CharField(validators=[phoneNumberRegex], max_length=16, null=True, blank=True, unique=True,
                             verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронная почта')

    class Meta:
        ordering = ['customer_id']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    # Используется для класса изменения Покупателя
    def get_absolute_url(self):
        return f'/customers/change/{self.customer_id}'


# Модель Прихода
class Arrival(models.Model):
    arrival_id = models.IntegerField(primary_key=True, verbose_name='№ Прихода')
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Продавец')
    products = models.ManyToManyField(Product, verbose_name='Товар')
    arrival_date = models.DateField(verbose_name='Дата прихода')
    quantity = models.IntegerField(verbose_name='Количество товара')
    user = models.ForeignKey(UserWH, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        ordering = ['arrival_id']

    # def result(self):  # Функция для вывода суммы
    #     res = 0
    #     for i in self.products.all():
    #         res += self.quantity * Product.objects.get(price='1')
    #     return res

    # Используется для класса изменения Расхода
    def get_absolute_url(self):
        return f'/arrivals/change/{self.arrival_id}'


# Модель Расхода
class Expense(models.Model):
    expense_id = models.IntegerField(primary_key=True, verbose_name='№ Расхода')
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Покупатель')
    products = models.ManyToManyField(Product, verbose_name='Товар')
    expense_date = models.DateField(verbose_name='Дата расхода')
    quantity = models.IntegerField(verbose_name='Количество товара')
    user = models.ForeignKey(UserWH, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        ordering = ['expense_id']

    # def result(self): # Функция для вывода суммы
    #   return self.quantity * self.product_id.price

    # Используется для класса изменения Прихода
    def get_absolute_url(self):
        return f'/expenses/change/{self.expense_id}'
