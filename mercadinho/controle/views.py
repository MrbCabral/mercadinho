from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Produto


def home(request):
    return render(request, "controle/home.html")


def cadastrar_produto(request):
    if request.method == 'POST':
        # Processar o formulário
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')
        
        # Validar os dados (simplificado)
        if nome and preco and quantidade:
            Produto.objects.create(
                nome=nome,
                descricao=descricao,
                preco=preco,
                quantidade=quantidade
            )
            return redirect('lista_produtos')
        else:
            return HttpResponse("Preencha todos os campos obrigatórios", status=400)
    
    # Se for GET, mostrar o formulário vazio
    return render(request, 'cadastrar_produto.html')


def lista_produtos(request):
    produtos = Produto.objects.all().order_by('-data_cadastro')
    return render(request, 'lista_produtos.html', {'produtos': produtos})

def produtos_view(request):
    # Se for POST, processa o formulário
    if request.method == 'POST':
        cod_produto = request.POST.get('cod_produto')
        nome = request.POST.get('nome')
        categoria = request.POST.get('categoria')
        estoque_atual = request.POST.get('estoque_atual')
        estoque_minimo = request.POST.get('estoque_minimo')
        
        if cod_produto and nome and categoria and estoque_atual and estoque_minimo:
            Produto.objects.create(
                cod_produto=cod_produto,
                nome=nome,
                categoria=categoria,
                estoque_atual=estoque_atual,
                estoque_minimo=estoque_minimo
            )
            return redirect('produtos')  # Redireciona para evitar reenvio do form
    
    # Para ambos GET e POST, mostra a lista de produtos
    produtos = Produto.objects.all().order_by('cod_produto')
    return render(request, 'controle/home.html', {'produtos': produtos})