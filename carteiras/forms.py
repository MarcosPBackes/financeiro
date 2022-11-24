from django import forms

from .models import Variavel, Acao, Fixa, Entrada, Saida

class AcaoForm(forms.ModelForm):
    class Meta:
        model = Acao
        fields = ('tks', 'nome')
class ContaeForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ('descricao', 'faturado', 'valor', 'data_e')
class ContasForm(forms.ModelForm):
    class Meta:
        model = Saida
        fields = ('descricao', 'faturado', 'valor', 'data_e')

class VariavelForm(forms.ModelForm):
    class Meta:
        model = Variavel
        fields = ('acao', 'data_compra', 'quantidade', 'valor_pago')
        widgets = {
            'data_compra': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'type': 'date'}
            ),
            'valor_pago': forms.NumberInput(
                attrs={'step': 0.01}
            )
        }
        
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

