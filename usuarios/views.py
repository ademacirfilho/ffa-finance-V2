from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import UsuarioForm
from django.urls import reverse_lazy

from .models import Perfil

class UsuarioCreate(CreateView):
    template_name = "usuarios/cadastro.html"
    form_class = UsuarioForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        url = super().form_valid(form)

        Perfil.objects.create(usuario=self.object)

        return url