from django import forms

from .models import Variavel, Acao

class AcaoForm(forms.ModelForm):
    class Meta:
        model = Acao
        fields = ('ticker', 'nome')

class VariavelForm(forms.ModelForm):
    class Meta:
        model = Variavel
        fields = ('acao', 'preco_medio', 'quantidade', 'valor_pago')
    
        
class FixaForm(forms.ModelForm):
    class Meta:
        model = Variavel
        fields = ()


