from django.urls import path
from .views import IndexView, ReceitasView, DespesasView, ContatosView, CategoriaList, UsuarioView 
from .views import CategoriaCreate
from .views import CategoriaUpdate
from .views import CategoriaDelete 

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("receitas/", ReceitasView.as_view(), name="receitas"),
    path("despesas/", DespesasView.as_view(), name="despesas"),
    path("contatos/", ContatosView.as_view(), name="contatos"),
    path("categorias/", CategoriaList.as_view(), name="categorias"),
    path("usuario/", UsuarioView.as_view(), name="usuario"),

    path("categorias/cadastrar/", CategoriaCreate.as_view(), name="cadastrar_categoria"),

    path("categorias/editar/<int:pk>/", CategoriaUpdate.as_view(), name="editar_categoria"),

    path("categorias/excluir/<int:pk>/", CategoriaDelete.as_view(), name="excluir_categoria"),
]