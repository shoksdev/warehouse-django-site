#########################################################ИМПОРТ#########################################################


# Импорт чего-либо из django
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.contrib import messages
# Импорт чего-либо из других источников
from datetime import datetime
# Импорт чего-либо из проекта
from .models import Product, UserWH, Supplier, Customer, Expense, Arrival
from .forms import RegisterForm, ProductForm, SupplierForm, CustomerForm, ArrivalForm, ExpenseForm


#########################################################ГЛАВНАЯ########################################################


# Главная страница
def index(request):
    return render(request, 'main/index.html')


################################################РЕГИСТРАЦИЯ И АВТОРИЗАЦИЯ###############################################


# Вход в аккаунт
class WHLoginView(LoginView):
    template_name = 'registration/login.html'  # Шаблон страницы
    success_url = reverse_lazy('main:profile')  # Перебрасывает в случае удачного входа в аккаунт в профиль


# Выход из аккаунта
class WHLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'registration/logout.html'  # Шаблон страницы


# Регистрация
class RegisterView(CreateView):
    model = UserWH  # Модель юзера
    template_name = 'registration/register.html'  # Шаблон страницы
    form_class = RegisterForm  # Форма для регистрации
    success_url = reverse_lazy('main:register_done')  # Перебрасывает в случае удачного входа на страницу с сообщением о
    # удачной регистрации пользователя


# Страница с сообщением об успешной регистрации
class RegisterDoneView(TemplateView):
    template_name = 'registration/register_done.html'  # Шаблон страницы


# Профиль
@login_required  # Пускаем только авторизованных пользователей
def profile(request):
    return render(request, 'registration/profile.html')  # Шаблон страницы


################################################ВСЁ ЧТО СВЯЗАНО С ТОВАРОМ###############################################


# Все товары
@login_required  # Пускаем только авторизованных пользователей
def products_all(request):
    if request.method == 'GET':  # Если метод запроса GET
        products = Product.objects.all()  # Все объекты модели Товар
        context = {'products': products}  # Контекст шаблона
        return render(request, 'main/products_all.html', context)  # Рендер шаблона с учётом контекста


# Добавление товара
@login_required  # Пускаем только авторизованных пользователей
def product_add(request):
    form = ProductForm(request.POST)  # Обработка формы
    if form.is_valid():  # Если форма валидна
        form.save()  # Сохраняем форму
        messages.add_message(request, messages.SUCCESS,
                             'Товар добавлен')  # И выводим сообщение о том что Товар добавлен
        return redirect('main:products_all')  # Затем возвращаем пользователя на страницу со всеми Товарами
    context = {'form': form}  # Контекст шаблона
    return render(request, 'main/product_add.html', context)  # Рендер шаблона с учётом контекста


# Удаление товара
@login_required  # Пускаем только авторизованных пользователей
def product_delete(request, product_id=None):
    if request.method == 'POST':  # Если метод запроса POST
        delete_list = request.POST.getlist('product_list')  # Берём список всех Товаров
        for prod_id in delete_list:  # Проходимся по нему
            product = get_object_or_404(Product, product_id=prod_id)  # Берём из этого списка только отмеченные флажком
            product.delete()  # Удаляем
        messages.add_message(request, messages.SUCCESS,
                             'Товар(ы) удален(ы)')  # И выводим сообщение о том что Товар удалён
        return redirect('main:products_all')  # Затем возвращаем пользователя на страницу со всеми Товарами
    else:
        products = Product.objects.all()  # Все объекты модели Товар
        context = {'products': products}  # Контекст шаблона
        return render(request, 'main/products_all.html', context)  # Рендер шаблона с учётом контекста


# Изменение товара
class ProductChangeView(UpdateView):
    model = Product  # Для класса берём модель Товар
    template_name = 'main/product_change.html'  # Шаблон
    form_class = ProductForm  # Форма, основанная на модели Товар
    success_url = reverse_lazy(
        'main:products_all')  # При удачном изменении возвращаем пользователя на страницу со всеми
    # Товарами


################################################ВСЁ ЧТО СВЯЗАНО С УСЛУГОЙ###############################################


# Все услуги
@login_required  # Пускаем только авторизованных пользователей
def services_all(request):
    if request.method == 'GET':  # Если метод запроса GET
        products = Product.objects.all()  # Все объекты модели Товар
        context = {'products': products}  # Контекст шаблона
        return render(request, 'main/services_all.html', context)  # Рендер шаблона с учётом контекста


# Добавление услуги
@login_required  # Пускаем только авторизованных пользователей
def service_add(request):
    form = ProductForm(request.POST)  # Обработка формы
    if form.is_valid():  # Если форма валидна
        form.save()  # Сохраняем форму
        messages.add_message(request, messages.SUCCESS,
                             'Услуга добавлена')  # И выводим сообщение о том что Услуга добавлена
        return redirect('main:services_all')  # Затем возвращаем пользователя на страницу со всеми Услуги
    context = {'form': form}  # Контекст шаблона
    return render(request, 'main/service_add.html', context)  # Рендер шаблона с учётом контекста


# Удаление услуги
@login_required  # Пускаем только авторизованных пользователей
def service_delete(request, product_id=None):
    if request.method == 'POST':  # Если метод запроса POST
        delete_list = request.POST.getlist('product_list')  # Берём список всех Услуг(Товаров)
        for prod_id in delete_list:  # Проходимся по нему
            product = get_object_or_404(Product, product_id=prod_id)  # Берём из этого списка только отмеченные флажком
            product.delete()  # Удаляем
        messages.add_message(request, messages.SUCCESS,
                             'Услуга(и) удалена(ы)')  # И выводим сообщение о том что Услуга удалена
        return redirect('main:services_all')  # Затем возвращаем пользователя на страницу со всеми Услугами
    else:
        product = Product.objects.all()  # Все объекты модели Товар
        context = {'product': product}  # Контекст шаблона
        return render(request, 'main/products_all.html', context)  # Рендер шаблона с учётом контекста


# Изменение услуги
class ServiceChangeView(UpdateView):
    model = Product  # Для класса берём модель Товар
    template_name = 'main/service_change.html'  # Шаблон
    form_class = ProductForm  # Форма, основанная на модели Товар
    success_url = reverse_lazy(
        'main:services_all')  # При удачном изменении возвращаем пользователя на страницу со всеми
    # Товарами


################################################ВСЁ ЧТО СВЯЗАНО С ПОКУПАТЕЛЕМ###########################################


# Все покупатели
@login_required  # Пускаем только авторизованных пользователей
def customers_all(request):
    if request.method == 'GET':  # Если метод запроса GET
        customers = Customer.objects.all()  # Все объекты модели Покупатель
        context = {'customers': customers}  # Контекст шаблона
        return render(request, 'main/customers_all.html', context)  # Рендер шаблона с учётом контекста


# Добавление покупателя
@login_required  # Пускаем только авторизованных пользователей
def customer_add(request):
    form = CustomerForm(request.POST)  # Обработка формы
    if form.is_valid():  # Если форма валидна
        form.save()  # Сохраняем форму
        messages.add_message(request, messages.SUCCESS,
                             'Покупатель добавлен')  # И выводим сообщение о том что Покупатель добавлен
        return redirect('main:customers_all')  # Затем возвращаем пользователя на страницу со всеми Покупателями
    context = {'form': form}  # Контекст шаблона
    return render(request, 'main/customer_add.html', context)  # Рендер шаблона с учётом контекста


# Удаление покупателя
@login_required  # Пускаем только авторизованных пользователей
def customer_delete(request, customer_id=None):
    if request.method == 'POST':  # Если метод запроса POST
        delete_list = request.POST.getlist('customer_list')  # Берём список всех Покупателей
        for cust_id in delete_list:  # Проходимся по нему
            customer = get_object_or_404(Customer,
                                         customer_id=cust_id)  # Берём из этого списка только отмеченные флажком
            customer.delete()  # Удаляем
        messages.add_message(request, messages.SUCCESS,
                             'Покупатели(ы) удален(ы)')  # И выводим сообщение о том что Покупатель удалён
        return redirect('main:customers_all')  # Затем возвращаем пользователя на страницу со всеми Товарами
    else:
        customer = Customer.objects.all()  # Все объекты модели Покупатель
        context = {'customer': customer}  # Контекст шаблона
        return render(request, 'main/customers_all.html', context)  # Рендер шаблона с учётом контекста


# Изменение покупателя
class CustomerChangeView(UpdateView):
    model = Customer  # Для класса берём модель Покупатель
    template_name = 'main/customer_change.html'  # Шаблон
    form_class = CustomerForm  # Форма, основанная на модели Покупатель
    success_url = reverse_lazy(
        'main:customers_all')  # При удачном изменении возвращаем пользователя на страницу со всеми
    # Покупателями


################################################ВСЁ ЧТО СВЯЗАНО С ПРОДАВЦОМ#############################################


# Все продавцы
@login_required  # Пускаем только авторизованных пользователей
def suppliers_all(request):
    if request.method == 'GET':  # Если метод запроса GET
        suppliers = Supplier.objects.all()  # Все объекты модели Продавец
        context = {'suppliers': suppliers}  # Контекст шаблона
        return render(request, 'main/suppliers_all.html', context)  # Рендер шаблона с учётом контекста


# Добавление продавца
@login_required  # Пускаем только авторизованных пользователей
def supplier_add(request):
    form = SupplierForm(request.POST)  # Обработка формы
    if form.is_valid():  # Если форма валидна
        form.save()  # Сохраняем форму
        messages.add_message(request, messages.SUCCESS,
                             'Продавец добавлен')  # И выводим сообщение о том что Продавец добавлен
        return redirect('main:suppliers_all')  # Затем возвращаем пользователя на страницу со всеми Продавцами
    context = {'form': form}  # Контекст шаблона
    return render(request, 'main/supplier_add.html', context)  # Рендер шаблона с учётом контекста


# Удаление продавца
@login_required  # Пускаем только авторизованных пользователей
def supplier_delete(request, supplier_id=None):
    if request.method == 'POST':  # Если метод запроса POST
        delete_list = request.POST.getlist('supplier_list')  # Берём список всех Продавцов
        for supp_id in delete_list:  # Проходимся по нему
            supplier = get_object_or_404(Supplier,
                                         supplier_id=supp_id)  # Берём из этого списка только отмеченные флажком
            supplier.delete()  # Удаляем
        messages.add_message(request, messages.SUCCESS,
                             'Продавц(ы) удален(ы)')  # И выводим сообщение о том что Продавец удалён
        return redirect('main:suppliers_all')  # Затем возвращаем пользователя на страницу со всеми Продавцами
    else:
        supplier = Supplier.objects.all()  # Все объекты модели Продавец
        context = {'supplier': supplier}  # Контекст шаблона
        return render(request, 'main/suppliers_all.html', context)  # Рендер шаблона с учётом контекста


# Изменение продавца
class SupplierChangeView(UpdateView):
    model = Supplier  # Для класса берём модель Продавец
    template_name = 'main/supplier_change.html'  # Шаблон
    form_class = SupplierForm  # Форма, основанная на модели Продавец
    success_url = reverse_lazy(
        'main:suppliers_all')  # При удачном изменении возвращаем пользователя на страницу со всеми Продавцами


###############################################ВСЁ ЧТО СВЯЗАНО С ПРИХОДОМ###############################################


# Все приходы
@login_required  # Пускаем только авторизованных пользователей
def arrivals_all(request):
    if request.method == 'GET':  # Если метод запроса GET
        arrivals = Arrival.objects.all()  # Все объекты модели Приход
        products = Product.objects.all()  # Все объекты модели Товар
        suppliers = Supplier.objects.all()  # Все объекты модели Продавец
        arrival = Arrival(user=request.user)  # Тайно присваиваем для модели Приход текущего пользователя
        form = ArrivalForm(request.POST, instance=arrival)  # Обработка формы для создания Прихода
        # Понадобится для создания отчёта
        if form.is_valid():  # Если форма валидна
            form.save()  # Сохраняем форму
            messages.add_message(request, messages.SUCCESS,
                                 'Приход добавлен')  # И выводим сообщение о том что Приход добавлен
        context = {'form': form, 'arrivals': arrivals, 'products': products, 'suppliers': suppliers}  # Контекст шаблона
        return render(request, 'main/arrivals_all.html', context)  # Рендер шаблона с учётом контекста


# Добавление прихода
@login_required  # Пускаем только авторизованных пользователей
def arrival_add(request):
    if request.method == 'POST':  # Если метод запроса POST
        arrivals = Arrival.objects.all()  # Все объекты модели Приход
        products = Product.objects.all()  # Все объекты модели Товар
        suppliers = Supplier.objects.all()  # Все объекты модели Продавец
        arrival = Arrival(user=request.user)  # Тайно присваиваем для модели Приход текущего пользователя
        form = ArrivalForm(request.POST, instance=arrival)  # Обработка формы
        if form.is_valid():  # Если форма валидна
            form.save()  # Сохраняем форму
            messages.add_message(request, messages.SUCCESS,
                                 'Приход добавлен')  # И выводим сообщение о том что Приход добавлен
            return redirect('main:arrivals_all')  # Затем возвращаем пользователя на страницу со всеми Приходами
        context = {'form': form, 'arrivals': arrivals, 'products': products, 'suppliers': suppliers}  # Контекст шаблона
        return render(request, 'main/arrivals_all.html', context)  # Рендер шаблона с учётом контекста


# Удаление прихода(не работает)
@login_required  # Пускаем только авторизованных пользователей
def arrival_delete(request, arrival_id=None):
    if request.method == 'GET':  # Если метод запроса GET
        delete_list = request.POST.getlist('arrival_list')  # Берём список всех Расходов
        for arri_id in delete_list:  # Проходимся по нему
            arrival = get_object_or_404(Arrival, arrival_id=arri_id)  # Берём из этого списка только отмеченные флажком
            arrival.delete()  # Удаляем
        messages.add_message(request, messages.SUCCESS,
                             'Приход(ы) товара удален(ы)')  # И выводим сообщение о том что Приход удалён
        return redirect('main:arrivals_all')  # Затем возвращаем пользователя на страницу со всеми Приходами
    else:
        arrivals = Arrival.objects.all()  # Все объекты модели Расход
        context = {'arrivals': arrivals}  # Контекст шаблона
        return render(request, 'main/arrivals_all.html', context)  # Рендер шаблона с учётом контекста


# Изменение прихода
class ArrivalChangeView(UpdateView):
    model = Arrival  # Для класса берём модель Приход
    template_name = 'main/arrival_change.html'  # Шаблон
    form_class = ArrivalForm  # Форма, основанная на модели Приход
    success_url = reverse_lazy(
        'main:arrivals_all')  # При удачном изменении возвращаем пользователя на страницу со всеми Приходами

    def get_context_data(self, **kwargs):  # Используем эту функцию для обработки дополнительных моделей
        context = super(ArrivalChangeView, self).get_context_data(**kwargs)  # Передаём контекст шаблона
        context['products'] = Product.objects.all()  # В контекст шаблона передаём все объекты модели Товар
        context['suppliers'] = Supplier.objects.all()  # В контекст шаблона передаём все объекты модели Продавец
        return context  # Возвращаем контекст


###############################################ВСЁ ЧТО СВЯЗАНО С РАСХОДОМ###############################################


# Все расходы
@login_required  # Пускаем только авторизованных пользователей
def expenses_all(request):
    if request.method == 'GET':  # Если метод запроса GET
        expenses = Expense.objects.all()  # Все объекты модели Расход
        products = Product.objects.all()  # Все объекты модели Товар
        customers = Customer.objects.all()  # Все объекты модели Покупатель
        expense = Expense(user=request.user)  # Тайно присваиваем для модели Расход текущего пользователя
        # Понадобится для создания отчёта
        form = ExpenseForm(request.POST, instance=expense)  # Обработка формы для создания Прихода
        if form.is_valid():  # Если форма валидна
            form.save()  # Сохраняем форму
            messages.add_message(request, messages.SUCCESS,
                                 'Расход добавлен')  # И выводим сообщение о том что Расход добавлен
        context = {'form': form, 'expenses': expenses, 'products': products, 'customers': customers}  # Контекст шаблона
        return render(request, 'main/expenses_all.html', context)  # Рендер шаблона с учётом контекста


# Добавление расхода
@login_required  # Пускаем только авторизованных пользователей
def expense_add(request):
    if request.method == 'POST':  # Если метод запроса POST
        expenses = Expense.objects.all()  # Все объекты модели Расход
        products = Product.objects.all()  # Все объекты модели Товар
        customers = Customer.objects.all()  # Все объекты модели Покупатель
        expense = Expense(user=request.user)  # Тайно присваиваем для модели Расход текущего пользователя
        form = ExpenseForm(request.POST, instance=expense)  # Обработка формы
        if form.is_valid():  # Если форма валидна
            form.save()  # Сохраняем форму
            messages.add_message(request, messages.SUCCESS,
                                 'Расход добавлен')  # И выводим сообщение о том что Расход добавлен
            return redirect('main:expenses_all')  # Затем возвращаем пользователя на страницу со всеми Расходами
        context = {'form': form, 'expenses': expenses, 'products': products, 'customers': customers}  # Контекст шаблона
        return render(request, 'main/expenses_all.html', context)  # Рендер шаблона с учётом контекста


# Удаление расхода(не работает)
@login_required  # Пускаем только авторизованных пользователей
def expense_delete(request, expense_id=None):
    if request.method == 'GET':  # Если метод запроса GET
        delete_list = request.POST.getlist('expense_list')  # Берём список всех Приходов
        for expe_id in delete_list:  # Проходимся по нему
            expense = get_object_or_404(Expense, expense_id=expe_id)  # Берём из этого списка только отмеченные флажком
            expense.delete()  # Удаляем
        messages.add_message(request, messages.SUCCESS,
                             'Расход(ы) товара удален(ы)')  # И выводим сообщение о том что Расход удалён
        return redirect('main:expenses_all')  # Затем возвращаем пользователя на страницу со всеми Расходами
    else:
        expense = Expense.objects.all()  # Все объекты модели Приход
        context = {'expense': expense}  # Контекст шаблона
        return render(request, 'main/expenses_all.html', context)  # Рендер шаблона с учётом контекста


# Изменение расхода
class ExpenseChangeView(UpdateView):
    model = Expense  # Для класса берём модель Расход
    template_name = 'main/expense_change.html'  # Шаблон
    form_class = ExpenseForm  # Форма, основанная на модели Расход
    success_url = reverse_lazy(
        'main:expenses_all')  # При удачном изменении возвращаем пользователя на страницу со всеми Расходами

    def get_context_data(self, **kwargs):  # Используем эту функцию для обработки дополнительных моделей
        context = super(ExpenseChangeView, self).get_context_data(**kwargs)  # Передаём контекст шаблона
        context['products'] = Product.objects.all()  # В контекст шаблона передаём все объекты модели Товар
        context['customers'] = Customer.objects.all()  # В контекст шаблона передаём все объекты модели Покупатель
        return context  # Возвращаем контекст


###########################################ВСЁ ЧТО СВЯЗАНО С ОТЧЁТОМ О ПРИХОДЕ##########################################


# Все отчёты о приходах
@login_required  # Пускаем только авторизованных пользователей
def arrival_reports_all(request):
    if request.method == 'GET':  # Если метод запроса GET
        arrival_reports = Arrival.objects.all()  # Все объекты модели Расход
        context = {'arrival_reports': arrival_reports}  # Контекст шаблона
        return render(request, 'main/arrival_reports_all.html', context)  # Рендер шаблона с учётом контекста


# Функция, которая отвечает за вывод отчётов о приходах по определённой дате
def arrival_report_filter(request, pk):
    if pk == 1:  # Если пользователь нажал на кнопку "Год" фильтруем Отчёты за текущий год
        arrival_report = Arrival.objects.filter(arrival_date__year=datetime.now().year)
    elif pk == 2:  # Если пользователь нажал на кнопку "Месяц" фильтруем Отчёты за текущий месяц
        arrival_report = Arrival.objects.filter(arrival_date__month=datetime.now().month)
    elif pk == 3:  # Если пользователь нажал на кнопку "День" фильтруем Отчёты за текущий день
        arrival_report = Arrival.objects.filter(arrival_date__day=datetime.now().day)
    elif pk == 4:  # Если пользователь нажал на кнопку "Всё" выводим все отчёты о расходах
        arrival_report = Arrival.objects.all()  # Все объекты модели Расход
    context = {'arrival_reports': arrival_report}  # Контекст шаблона
    return render(request, 'main/arrival_reports_all.html', context)  # Рендер шаблона с учётом контекста


###########################################ВСЁ ЧТО СВЯЗАНО С ОТЧЁТОМ О РАСХОДЕ##########################################

# Все отчёты о расходах
@login_required  # Пускаем только авторизованных пользователей
def expense_reports_all(request):
    if request.method == 'GET':  # Если метод запроса GET
        expense_reports = Expense.objects.all()  # Все объекты модели Приход
        context = {'expenses_reports': expense_reports}  # Контекст шаблона
        return render(request, 'main/expense_reports_all.html', context)  # Рендер шаблона с учётом контекста


# Функция, которая отвечает за вывод отчётов о расходах по определённой дате
def expense_report_filter(request, pk):
    if pk == 1:  # Если пользователь нажал на кнопку "Год" фильтруем Отчёты за текущий год
        expense_report = Expense.objects.filter(expense_date__year=datetime.now().year)
    elif pk == 2:  # Если пользователь нажал на кнопку "Месяц" фильтруем Отчёты за текущий месяц
        expense_report = Expense.objects.filter(expense_date__month=datetime.now().month)
    elif pk == 3:  # Если пользователь нажал на кнопку "День" фильтруем Отчёты за текущий день
        expense_report = Expense.objects.filter(expense_date__day=datetime.now().day)
    elif pk == 4:  # Если пользователь нажал на кнопку "Всё" выводим все отчёты о расходах
        expense_report = Expense.objects.all()  # Все объекты модели Приход
    context = {'expense_report': expense_report}  # Контекст шаблона
    return render(request, 'main/expense_reports_all.html', context)  # Рендер шаблона с учётом контекста
