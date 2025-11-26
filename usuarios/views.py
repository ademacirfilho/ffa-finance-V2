from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from .forms import UsuarioForm
from finance.forms import PerfilForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Perfil

class UsuarioCreate(CreateView):
    template_name = "usuarios/cadastro.html"
    form_class = UsuarioForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        url = super().form_valid(form)

        Perfil.objects.create(usuario=self.object)

        return url
    
class PerfilUpdate(UpdateView):
    template_name = "usuarios/atualizar_dados.html"
    form_class = PerfilForm
    success_url = reverse_lazy("usuario")

    def get_object(self, queryset=None):
        return get_object_or_404(Perfil, usuario=self.request.user)

    def form_valid(self, form):
        form.instance.foto_perfil = self.request.FILES.get("foto_perfil", form.instance.foto_perfil)
        return super().form_valid(form)