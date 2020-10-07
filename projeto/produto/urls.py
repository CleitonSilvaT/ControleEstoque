from django.urls import path
from projeto.produto import views

app_name = 'produto'

urlpatterns = [
    path('', views.lista_produto, name='lista_produto'),
    path('<int:pk>/', views.detalhe_produto, name='detalhe_produto'),
    path('add/', views.ProdutoCreate.as_view(), name='adiciona_produto'),
]