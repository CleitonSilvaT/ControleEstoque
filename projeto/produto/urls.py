from django.urls import path
from projeto.produto import views

app_name = 'produto'

urlpatterns = [
    path('', views.lista_produto, name='lista_produto'),
]