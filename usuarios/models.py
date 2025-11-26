from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    nome = models.CharField(max_length=20, null=True)
    sobrenome = models.CharField(max_length=20, null=True)
    cpf = models.CharField(max_length=14, null=True, verbose_name="CPF")
    telefone = models.CharField(max_length=16, null=True)
    foto_perfil = models.ImageField(upload_to='perfil/', null=True, blank=True, verbose_name="Foto de Perfil")
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)