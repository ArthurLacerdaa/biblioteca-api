from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_livros),
    path('novo/', views.criar_livro),
    path('<int:id>/', views.buscar_livro),
    path('editar/<int:id>/', views.atualizar_livro),
    path('deletar/<int:id>/', views.deletar_livro),
]