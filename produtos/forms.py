from django import forms
from .models import Produtos
from django.http import JsonResponse

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['codigo','descricao','marca',
                  'quantidade_minima','quantidade',
                  'custo','preco','observacao']
        
    def clean_codigo(self):
     codigo = self.cleaned_data['codigo']
     if Produtos.objects.filter(codigo=codigo).exists():
        return JsonResponse({'error': 'Codigo já cadastrado'})
     return codigo
        