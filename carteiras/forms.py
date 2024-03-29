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
        widgets = {
            'data_e': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'type': 'date'}
            ),
            'valor': forms.NumberInput(
                attrs={'step': 0.01}
            )
        }
class ContasForm(forms.ModelForm):
    class Meta:
        model = Saida
        fields = ('descricao', 'faturado', 'valor', 'data_e')
        widgets = {
            'data_e': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'type': 'date'}
            ),
            'valor': forms.NumberInput(
                attrs={'step': 0.01}
            )
        }

class VariavelForm(forms.ModelForm):
    class Meta:
        model = Variavel
        fields = ('acao', 'data_e', 'quantidade', 'valor')
        widgets = {
            'data_e': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'type': 'date'}
            ),
            'valor': forms.NumberInput(
                attrs={'step': 0.01}
            )
        }
        
class FixaForm(forms.ModelForm):
    class Meta:
        model = Fixa
        fields = ('valor', 'rendimento', 'tempo', 'data_e', 'tipo', 'descricao_tipo')
        widgets = {
            'valor': forms.NumberInput(
                attrs={'step': 0.01}
            ),
            'data_e': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'type': 'date'}
            )
        }

