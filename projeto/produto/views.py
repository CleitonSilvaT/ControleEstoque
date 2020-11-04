from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.http import JsonResponse
from .models import Produto
from .forms import ProdutoForm

# Create your views here.

def lista_produto(request):
    template_name = 'lista_produto.html'
    objects = Produto.objects.all()
    context = {'lista_object':objects}

    return render(request, template_name, context)

def detalhe_produto(request, pk):
    template_name = 'detalhe_produto.html'
    obj = Produto.objects.get(pk=pk)
    context = {'object':obj}

    return render(request, template_name, context)

def adiciona_produto(request):
    template_name = 'produto_form.html'

    return render(request, template_name)

def produto_json(request, pk):
    produto = Produto.objects.filter(pk=pk)
    data = [item.to_dict_json() for item in produto]
    return JsonResponse({'data': data})

class ProdutoCreate(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm

class ProdutoUpdate(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm