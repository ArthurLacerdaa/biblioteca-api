from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/livros/', include('livros.urls')),
    path('api/usuarios/', include('usuarios.urls')),
]