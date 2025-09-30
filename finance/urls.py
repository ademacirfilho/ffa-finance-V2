from django.urls import path
from .views import IndexView, ReceitaList, ContatosList, CategoriaList, UsuarioView, DespesaList 
from .views import CategoriaCreate, ContatosCreate, ReceitaCreate, DespesaCreate
from .views import CategoriaUpdate, ContatosUpdate, ReceitaUpdate, DespesaUpdate
from .views import CategoriaDelete, ContatosDelete, ReceitaDelete, DespesaDelete

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("receitas/", ReceitaList.as_view(), name="receitas"),
    path("despesas/", DespesaList.as_view(), name="despesas"),
    path("contatos/", ContatosList.as_view(), name="contatos"),
    path("categorias/", CategoriaList.as_view(), name="categorias"),
    path("usuario/", UsuarioView.as_view(), name="usuario"),

    path("receitas/cadastrar/", ReceitaCreate.as_view(), name="cadastrar_receita"),
    path("despesas/cadastrar/", DespesaCreate.as_view(), name="cadastrar_despesa"),
    path("categorias/cadastrar/", CategoriaCreate.as_view(), name="cadastrar_categoria"),
    path("contatos/cadastrar/", ContatosCreate.as_view(), name="cadastrar_contato"),

    path("receitas/editar/<int:pk>/", ReceitaUpdate.as_view(), name="editar_receita"),
    path("despesas/editar/<int:pk>/", DespesaUpdate.as_view(), name="editar_despesa"),
    path("categorias/editar/<int:pk>/", CategoriaUpdate.as_view(), name="editar_categoria"),
    path("contatos/editar/<int:pk>/", ContatosUpdate.as_view(), name="editar_contato"),

    path("receitas/excluir/<int:pk>/", ReceitaDelete.as_view(), name="excluir_receita"),
    path("despesas/excluir/<int:pk>/", DespesaDelete.as_view(), name="excluir_despesa"),
    path("categorias/excluir/<int:pk>/", CategoriaDelete.as_view(), name="excluir_categoria"),
    path("contatos/excluir/<int:pk>/", ContatosDelete.as_view(), name="excluir_contato"),
]