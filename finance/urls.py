from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("receitas/", views.receitas, name="receitas"),
    path("despesas/", views.despesas, name="despesas"),
    path("contatos/", views.contatos, name="contatos"),
    path("categorias/", views.categorias, name="categorias"),
    path("usuario/", views.usuario, name="usuario"),
]