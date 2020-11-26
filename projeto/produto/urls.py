from django.urls import path
from projeto.produto import views

app_name = 'produto'

urlpatterns = [
    path('', views.ProdutoList.as_view(), name='lista_produto'),
    path('<int:pk>/', views.detalhe_produto, name='detalhe_produto'),
    path('add/', views.ProdutoCreate.as_view(), name='adiciona_produto'),
    path('<int:pk>/edit/', views.ProdutoUpdate.as_view(), name='edita_produto'),
    path('<int:pk>/json/', views.produto_json, name='produto_json'),
]