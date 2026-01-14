from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required
def saudacao_bom_dia(request):
    saudacao = 'Bom dia'
    return render(request, 'saudacao.html', {'saudacao': saudacao})
