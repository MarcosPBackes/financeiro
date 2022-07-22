from django import forms

from .models import Variavel, Acao

class VariavelForm(forms.ModelForm):
    
    class Meta:
        model = Variavel
        fields = ('acao', 'quantidade')
    
        
class AcaoForm(forms.ModelForm):
       
    class Meta:
        model = Acao
        fields = ('nome', 'valor', 'codigo', 'data_compra')