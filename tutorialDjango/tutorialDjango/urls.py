from django.contrib import admin
from django.urls import path, include  # IMPORTANTE: include deve estar importado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aula1/', include('aula1.urls')),  # ← esta linha é essencial
]