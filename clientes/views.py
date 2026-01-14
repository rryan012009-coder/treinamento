from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Cliente
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required


@login_required

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html',{'clientes': clientes})

def buscar_nome(request):
    termo = request.GET.get('q','')
    clientes = Cliente.objects.filter(nome__icontains=termo)
    dados = list(clientes.values('cpf','nome','telefone','email'))
    return JsonResponse(dados,safe=False)

def cadastrar_cliente(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        cliente = Cliente.objects.filter(cpf=cpf).first()

        if cliente:
           form = ClienteForm(request.POST, instance=cliente)
        else:
           form = ClienteForm(request.POST)

        if form.is_valid():
           form.save()
           return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'cadastrar_cliente.html', {'form': form})

def consultar_cliente(request, cpf):
    try:
        cpf = ''.join(filter(str.isdigit, cpf))
        cliente = Cliente.objects.get(cpf=cpf)
        data =  {
            'nome': cliente.nome,
            'telefone': cliente.telefone,
            'email': cliente.email,
        }
        return JsonResponse(data)
    except Cliente.DoesNotExist:
        return JsonResponse({'error':'Cliente não encontrado.'}, status=404)
    
def excluir_cliente(request, cpf):
    if request.method == 'DELETE':
        try:
            cliente = Cliente.objects.get(cpf=cpf)
            cliente.delete()
            return JsonResponse({'message': 'Cliente excluido com sucesso'})
        except Cliente.DoesNotExist:
            return JsonResponse({'error':'Cliente não encontrado.'}, status=404)