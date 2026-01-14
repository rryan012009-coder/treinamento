from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Produtos
from .forms import ProdutoForm
from django.contrib.auth.decorators import login_required

@login_required

def lista_produtos(request):
    produtos = Produtos.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})

def cadastrar_produto(request):
    if request.method == 'POST':
       codigo = request.POST.get('codigo')
       produto = Produtos.objects.filter(codigo=codigo).first()
       
       if produto:
           form = ProdutoForm(request.POST,instance=produto)
       else:
           form = ProdutoForm(request.POST)
           
       if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'cadastrar_produtos.html', {'form': form})
def consultar_produto(request, codigo):
    try:
        produto = Produtos.objects.get(codigo=codigo)
        data =  {
            'descricao': produto.descricao,
            'marca': produto.marca,
            'quantidade_minima': produto.quantidade_minima,
            'quantidade': produto.quantidade,
            'custo': produto.custo,
            'preco':produto.preco,
            'observacao':produto.observacao,
        }
        
        return JsonResponse(data)
    except Produtos.DoesNotExist:
        return JsonResponse({'error': 'Produto não encontrado'}, status=404)

def excluir_produto(request, codigo):
  if request.method == 'DELETE':
     try:
         produto = Produtos.objects.get(codigo=codigo)
         produto.delete()
         return JsonResponse({'message': 'produto excluido com sucesso.'})
     except Produtos.DoesNotExist:
         return JsonResponse({'error': 'produto não encontrado.'}, status=404)
       