from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Receita, Despesa, Contato, Categoria
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = "finance/index.html"

class ReceitasView(TemplateView):
    template_name = "finance/receitas.html"

'''
class CreateReceitaView(CreateView):
    model = Receita
    fields = ['descricao', 'valor', 'data', 'recebido', 'tipo', 'categoriaNome', 'contatoNome', 'contato']
    success_url = "/receitas/"
'''

class DespesasView(TemplateView):
    template_name = "finance/despesas.html"
    
class UsuarioView(TemplateView):
    template_name = "finance/usuario.html"

###### CREATE ######

class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['nome', 'tipo']
    template_name = "form/form.html"
    success_url = reverse_lazy("categorias")

class ContatosCreate(CreateView):
    model = Contato
    fields = ['nome', 'email', 'telefone', 'cpf_cnpj', 'tipo']
    template_name = "form/form.html"
    success_url = reverse_lazy("contatos")

###### UPDATE ######

class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = ['nome', 'tipo']
    template_name = "form/form_editar.html"
    success_url = reverse_lazy("categorias")

class ContatosUpdate(UpdateView):
    model = Contato
    fields = ['nome', 'email', 'telefone', 'cpf_cnpj', 'tipo']
    template_name = "form/form_editar.html"
    success_url = reverse_lazy("contatos")

###### DELETE ######

class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = "form/form_excluir.html"
    success_url = reverse_lazy("categorias")

class ContatosDelete(DeleteView):
    model = Contato
    template_name = "form/form_excluir.html"
    success_url = reverse_lazy("contatos")

##### LIST #####

class CategoriaList(ListView):
    model = Categoria
    template_name = "finance/categorias.html"

class ContatosList(ListView):
    model = Contato
    template_name = "finance/contatos.html"