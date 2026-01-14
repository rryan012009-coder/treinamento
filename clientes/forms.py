from django import forms
from .models import Cliente
from django.http import JsonResponse
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cpf','nome','telefone','email']
        
    def clean_cpf(self):
     cpf = self.cleaned_data['cpf']
     if Cliente.objects.filter(cpf=cpf).exists():
        return JsonResponse({'message': 'Cpf já cadastrado'})
     return cpf