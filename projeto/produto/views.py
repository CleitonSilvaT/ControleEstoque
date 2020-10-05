from django.shortcuts import render
from .models import Produto

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