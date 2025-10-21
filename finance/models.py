from django.db import models
from django.contrib.auth.models import User

class Contato(models.Model):
    TIPO_CONTATO = [
        ('ASSOCIADO', 'Associado'),
        ('CLIENTE', 'Cliente'),
        ('COLABORADOR', 'Colaborador'),
        ('FORNECEDOR', 'Fornecedor'),
        ('SOCIO', 'Sócio'),
        ('OUTRO', 'Outro'),
    ]
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=15, blank=True)
    cpf_cnpj = models.CharField(max_length=18, blank=True, verbose_name="CPF/CNPJ")
    tipo = models.CharField(max_length=12, choices=TIPO_CONTATO)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Categoria(models.Model):
    TIPO_CATEGORIA = [
      ('FIXA', 'Fixa'),
      ('VARIAVEL', 'Variável'),
      ('IMPOSTO', 'Imposto'),
      ('RENDIMENTOS', 'Rendimentos'),
    ]
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=12, choices=TIPO_CATEGORIA)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - ({})".format(self.nome, self.tipo)

class Receita(models.Model):
    TIPO_RECEITA = [
        ('AVISTA', 'À Vista'),
        ('CARTÃO', 'Cartão'),
        ('PIX', 'Pix'),
        ('BOLETO', 'Boleto'),
    ]
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    recebido = models.BooleanField(default=False)
    tipo = models.CharField(max_length=10, choices=TIPO_RECEITA)
    categoriaNome = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    contatoNome = models.ForeignKey(Contato, on_delete=models.CASCADE, verbose_name="Contato")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao
    
class Despesa(models.Model):
    TIPO_DESPESA = [
        ('AVISTA', 'À Vista'),
        ('CARTÃO', 'Cartão'),
        ('PIX', 'Pix'),
        ('BOLETO', 'Boleto'),
    ]
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    pago = models.BooleanField(default=False)
    tipo = models.CharField(max_length=10, choices=TIPO_DESPESA)
    categoriaNome = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    contatoNome = models.ForeignKey(Contato, on_delete=models.CASCADE, verbose_name="Contato")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao