from django.shortcuts import render

def index(request):
    return render(request, "finance/index.html")

def receitas(request):
    return render(request, "finance/receitas.html")

def despesas(request):
    return render(request, "finance/despesas.html")

def contatos(request):
    return render(request, "finance/contatos.html")

def categorias(request):
    return render(request, "finance/categorias.html")

def usuario(request):
    return render(request, "finance/usuario.html")