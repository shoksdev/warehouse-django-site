from django.urls import path, re_path
from . import views

app_name = 'main'

urlpatterns = [
    # Ссылки на функции и классы связанные с работой аккаунта пользователя
    path('accounts/login', views.WHLoginView.as_view(), name='login'),
    path('accounts/logout', views.WHLogoutView.as_view(), name='logout'),
    path('accounts/register/register_done', views.RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', views.RegisterView.as_view(), name='register'),
    path('accounts/profile/', views.profile, name='profile'),
    # Ссылки на функции и классы связанные с работой отчётов о расходах
    path('expense_reports/filter/<int:pk>/', views.expense_report_filter, name='expense_report_filter'),
    path('expense_reports/', views.expense_reports_all, name='expense_reports_all'),
    # Ссылки на функции и классы связанные с работой отчётов о приходах
    path('arrival_reports/filter/<int:pk>/', views.arrival_report_filter, name='arrival_report_filter'),
    path('arrival_reports/', views.arrival_reports_all, name='arrival_reports_all'),
    # Ссылки на функции и классы связанные с расходами
    re_path(r'^expenses/delete/$', views.expense_delete, name='expense_delete'),
    path('expenses/change/<int:pk>/', views.ExpenseChangeView.as_view(), name='expense_change'),
    path('expenses/add', views.expense_add, name='expense_add'),
    path('expenses/', views.expenses_all, name='expenses_all'),
    # Ссылки на функции и классы связанные с приходами
    re_path(r'^arrivals/delete/$', views.arrival_delete, name='arrival_delete'),
    path('arrivals/change/<int:pk>/', views.ArrivalChangeView.as_view(), name='arrival_change'),
    path('arrivals/add', views.arrival_add, name='arrival_add'),
    path('arrivals/', views.arrivals_all, name='arrivals_all'),
    # Ссылки на функции и классы связанные с продавцами
    re_path(r'^suppliers/delete/$', views.supplier_delete, name='supplier_delete'),
    path('suppliers/change/<int:pk>/', views.SupplierChangeView.as_view(), name='supplier_change'),
    path('suppliers/add', views.supplier_add, name='supplier_add'),
    path('suppliers/', views.suppliers_all, name='suppliers_all'),
    # Ссылки на функции и классы связанные с покупателями
    re_path(r'^customers/delete/$', views.customer_delete, name='customer_delete'),
    path('customers/change/<int:pk>/', views.CustomerChangeView.as_view(), name='customer_change'),
    path('customers/add', views.customer_add, name='customer_add'),
    path('customers/', views.customers_all, name='customers_all'),
    # Ссылки на функции и классы связанные с услугами
    re_path(r'^services/delete/$', views.service_delete, name='service_delete'),
    path('services/change/<int:pk>/', views.ServiceChangeView.as_view(), name='service_change'),
    path('services/add', views.service_add, name='service_add'),
    path('services/', views.services_all, name='services_all'),
    # Ссылки на функции и классы связанные с товарами
    path('products/change/<int:pk>/', views.ProductChangeView.as_view(), name='product_change'),
    re_path(r'^products/delete/$', views.product_delete, name='product_delete'),
    path('products/add', views.product_add, name='product_add'),
    path('products/', views.products_all, name='products_all'),
    # Главная
    path('', views.index, name='index'),
]
