from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_usuarios),
    path('novo/', views.criar_usuario),
    path('<int:id>/', views.buscar_usuario),
    path('editar/<int:id>/', views.atualizar_usuario),
    path('deletar/<int:id>/', views.deletar_usuario),
]