from django import forms

from .models import Variavel

class VariavelForm(forms.ModelForm):

    class Meta:
        model = Variavel
        fields = ('valor', 'codigo', 'nome', 'data_compra', 'quantidade')