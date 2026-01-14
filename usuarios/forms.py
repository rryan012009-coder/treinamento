from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UsuarioForm(UserCreationForm):
    """Formulario para cadastro de usuario, utilizando e-mail como autenticador"""
    
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['email','password1','password2']
        labels = {
            'email': 'E-mail',
            'password1' : 'Senha',
            'password2' : 'Confirmação de Senha',
        }
        
        widgets =  {
            'password1': forms.PasswordInput(attrs={'class' : 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class' : 'form-control'}),
        }
            
    def save (self, commit=True):
      """Salva o usuario com e-mail como identificador."""
    
      user = super().save(commit=False)
      user.username = self.cleaned_data['email'] #Define o e-mail como username
      if commit:
         user.save()
      return user

class UsuarioLoginForm(AuthenticationForm):
    '''Formulario para login, usando e-mail em vez de username'''
    
    username = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    
class UsuarioUpdateForm(forms.ModelForm):
    '''Formulario para edição dos dados do usuario'''
    
    class Meta:
        model = User
        fields = ['email']
        labels =  {
            'email' : 'E-mail',
        }
        
        widgets =  {
            'email' : forms.EmailInput(attrs= {'class' : 'form-control'}),
        }
        
    def save(self, commit=True):
        '''Atualiza o usuario garantindo que username seja o mesmo que o e-mail'''
        
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user