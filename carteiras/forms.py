from django import forms

from .models import Variavel, Acao, Fixa

class AcaoForm(forms.ModelForm):
    class Meta:
        model = Acao
        fields = ('tks', 'nome')

class VariavelForm(forms.ModelForm):
    class Meta:
        model = Variavel
        fields = ('acao', 'preco_medio', 'quantidade', 'valor_pago')

    
        
class FixaForm(forms.ModelForm):
    class Meta:
        model = Fixa
        fields = ('valor_inv', 'rendimento', 'tempo', 'data_inv', 'tipo', 'descricao_tipo')
        widgets = {
            'valor_inv': forms.NumberInput(
                attrs={'step': 0.01}
            ),
            'data_inv': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'type': 'date'}
            )
        }

