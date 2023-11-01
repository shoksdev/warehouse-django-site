from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
