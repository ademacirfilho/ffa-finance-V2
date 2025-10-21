from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Receita, Despesa, Contato, Categoria
from .forms import ReceitaForm, DespesaForm, ContatoForm, CategoriaForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import get_object_or_404


class IndexView(TemplateView):
    template_name = "finance/index.html"
    
class UsuarioView(TemplateView):
    template_name = "finance/usuario.html"


###### CREATE ######
class ReceitaCreate(LoginRequiredMixin, CreateView):
    model = Receita
    form_class = ReceitaForm
    template_name = "form/form.html"
    success_url = reverse_lazy("receitas")

    def form_valid(self, form):
        form.instance.usuario = self.request.user

        url = super().form_valid(form)
        return url

class DespesaCreate(LoginRequiredMixin, CreateView):
    model = Despesa
    form_class = DespesaForm
    template_name = "form/form.html"
    success_url = reverse_lazy("despesas")

    def form_valid(self, form):
        form.instance.usuario = self.request.user

        url = super().form_valid(form)
        return url

class CategoriaCreate(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "form/form.html"
    success_url = reverse_lazy("categorias")

    def form_valid(self, form):
        form.instance.usuario = self.request.user

        url = super().form_valid(form)
        return url

class ContatosCreate(LoginRequiredMixin, CreateView):
    model = Contato
    form_class = ContatoForm
    template_name = "form/form.html"
    success_url = reverse_lazy("contatos")

    def form_valid(self, form):
        form.instance.usuario = self.request.user

        url = super().form_valid(form)
        return url


###### UPDATE ######
class ReceitaUpdate(LoginRequiredMixin, UpdateView):
    model = Receita
    form_class = ReceitaForm
    template_name = "form/form_editar.html"
    success_url = reverse_lazy("receitas")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Receita, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

class DespesaUpdate(LoginRequiredMixin, UpdateView):
    model = Despesa
    form_class = DespesaForm
    template_name = "form/form_editar.html"
    success_url = reverse_lazy("despesas")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Despesa, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "form/form_editar.html"
    success_url = reverse_lazy("categorias")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Categoria, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

class ContatosUpdate(LoginRequiredMixin, UpdateView):
    model = Contato
    form_class = ContatoForm
    template_name = "form/form_editar.html"
    success_url = reverse_lazy("contatos")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Contato, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


###### DELETE ######
class ReceitaDelete(LoginRequiredMixin, DeleteView):
    model = Receita
    template_name = "form/form_excluir.html"
    success_url = reverse_lazy("receitas")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Receita, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

class DespesaDelete(LoginRequiredMixin, DeleteView):
    model = Despesa
    template_name = "form/form_excluir.html"
    success_url = reverse_lazy("despesas")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Despesa, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

class CategoriaDelete(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = "form/form_excluir.html"
    success_url = reverse_lazy("categorias")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Categoria, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

class ContatosDelete(LoginRequiredMixin, DeleteView):
    model = Contato
    template_name = "form/form_excluir.html"
    success_url = reverse_lazy("contatos")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Contato, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


##### LIST #####
class ReceitaList(LoginRequiredMixin, ListView):
    model = Receita
    template_name = "finance/receitas.html"

    def get_queryset(self):
        self.object_list = Receita.objects.filter(usuario=self.request.user)
        return self.object_list

class DespesaList(LoginRequiredMixin, ListView):
    model = Despesa
    template_name = "finance/despesas.html"

    def get_queryset(self):
        self.object_list = Despesa.objects.filter(usuario=self.request.user)
        return self.object_list

class CategoriaList(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = "finance/categorias.html"

    def get_queryset(self):
        self.object_list = Categoria.objects.filter(usuario=self.request.user)
        return self.object_list

class ContatosList(LoginRequiredMixin, ListView):
    model = Contato
    template_name = "finance/contatos.html"

    def get_queryset(self):
        self.object_list = Contato.objects.filter(usuario=self.request.user)
        return self.object_list