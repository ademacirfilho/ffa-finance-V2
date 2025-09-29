from django.urls import path
from .views import IndexView, ReceitasView, DespesasView, ContatosList, CategoriaList, UsuarioView 
from .views import CategoriaCreate, ContatosCreate
from .views import CategoriaUpdate, ContatosUpdate
from .views import CategoriaDelete, ContatosDelete

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("receitas/", ReceitasView.as_view(), name="receitas"),
    path("despesas/", DespesasView.as_view(), name="despesas"),
    path("contatos/", ContatosList.as_view(), name="contatos"),
    path("categorias/", CategoriaList.as_view(), name="categorias"),
    path("usuario/", UsuarioView.as_view(), name="usuario"),

    path("categorias/cadastrar/", CategoriaCreate.as_view(), name="cadastrar_categoria"),
    path("contatos/cadastrar/", ContatosCreate.as_view(), name="cadastrar_contato"),

    path("categorias/editar/<int:pk>/", CategoriaUpdate.as_view(), name="editar_categoria"),
    path("contatos/editar/<int:pk>/", ContatosUpdate.as_view(), name="editar_contato"),

    path("categorias/excluir/<int:pk>/", CategoriaDelete.as_view(), name="excluir_categoria"),
    path("contatos/excluir/<int:pk>/", ContatosDelete.as_view(), name="excluir_contato"),
]