import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')
django.setup()

import string
import timeit
from random import choice, random, randint
from projeto.produto.models import Produto


class Utils:
    @staticmethod
    def digits_generator(max_length):
        return str(''.join(choice(string.digits) for i in range(max_length)))
    
class ProdutoClass:
    @staticmethod
    def create_produtos(produtos):
        Produto.objects.all().delete()
        aux = []
        for produto in produtos:
            data = dict(
                produto = produto,
                importado = choice((True, False)),
                ncm = Utils.digits_generator(8),
                preco = random() * randint(10, 50),
                estoque = randint(10,200)
            )
            obj = Produto(**data)
            aux.append(obj)
        Produto.objects.bulk_create(aux)


produtos = (
    'Apontador',
    'Caderno 100 folhas',
    'Caderno capa dura 200 folhas',
    'Caneta esferográfica azul',
    'Caneta esferográfica preta',
    'Caneta esferográfica vermelha',
    'Durex',
    'Giz de cera 12 cores',
    'Lapiseira 0.3 mm',
    'Lapiseira 0.5 mm',
    'Lapiseira 0.7 mm',
    'Lápis de cor 24 cores',
    'Lápis',
    'Papel sulfite A4 pacote 100 folhas',
    'Pasta elástica',
    'Tesoura',
)

start = timeit.default_timer()

ProdutoClass.create_produtos(produtos)

finish = timeit.default_timer()

print('Tempo:', finish - start)