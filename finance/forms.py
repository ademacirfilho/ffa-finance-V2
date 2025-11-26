from django import forms
from .models import Contato, Categoria, Receita, Despesa
from usuarios.models import Perfil

base_classes = (
    "bg-brand-medium text-white text-sm rounded-lg "
    "focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 my-2"
)

class CustomTextInput(forms.TextInput):
    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault("attrs", {})
        attrs["class"] = base_classes
        super().__init__(*args, **kwargs)


class CustomEmailInput(forms.EmailInput):
    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault("attrs", {})
        attrs["class"] = base_classes
        super().__init__(*args, **kwargs)


class CustomNumberInput(forms.NumberInput):
    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault("attrs", {})
        attrs["class"] = base_classes
        super().__init__(*args, **kwargs)


class CustomDateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault("attrs", {})
        attrs["class"] = base_classes
        super().__init__(*args, **kwargs)


class CustomSelect(forms.Select):
    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault("attrs", {})
        attrs["class"] = base_classes
        super().__init__(*args, **kwargs)


class CustomCheckboxInput(forms.CheckboxInput):
    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault("attrs", {})
        attrs["class"] = (
            "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 "
            "rounded focus:ring-primary-600"
        )
        super().__init__(*args, **kwargs)

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ["nome", "email", "telefone", "cpf_cnpj", "tipo"]
        widgets = {
            "nome": CustomTextInput(),
            "email": CustomEmailInput(),
            "telefone": CustomTextInput(),
            "cpf_cnpj": CustomTextInput(),
            "tipo": CustomSelect(),
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nome", "tipo"]
        widgets = {
            "nome": CustomTextInput(),
            "tipo": CustomSelect(),
        }


class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ["descricao", "valor", "data", "tipo", "categoriaNome", "contatoNome", "recebido"]
        widgets = {
            "descricao": CustomTextInput(),
            "valor": CustomNumberInput(),
            "data": CustomDateInput(),
            "tipo": CustomSelect(),
            "categoriaNome": CustomSelect(),
            "contatoNome": CustomSelect(),
            "recebido": CustomCheckboxInput(),
        }


class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ["descricao", "valor", "data", "tipo", "categoriaNome", "contatoNome", "pago"]
        widgets = {
            "descricao": CustomTextInput(),
            "valor": CustomNumberInput(),
            "data": CustomDateInput(),
            "tipo": CustomSelect(),
            "categoriaNome": CustomSelect(),
            "contatoNome": CustomSelect(),
            "pago": CustomCheckboxInput(),
        }

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ["nome", "sobrenome", "cpf", "telefone", "foto_perfil"]
        widgets = {
            "nome": CustomTextInput(),
            "sobrenome": CustomTextInput(),
            "cpf": CustomTextInput(),
            "telefone": CustomTextInput(),
            "foto_perfil": forms.ClearableFileInput(attrs={"class": base_classes}), 
        }