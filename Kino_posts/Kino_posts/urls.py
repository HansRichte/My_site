from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('myapp.urls')),  # Путь для вашего приложения
    path('admin/', admin.site.urls),  # Путь для административной панели Django
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
