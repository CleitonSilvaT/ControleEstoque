# Controle de Estoque

Este projeto apresenta um Controle de Estoque Django.



## Rodando o Projeto Localmente

* Clone o repositório

```
git clone https://github.com/CleitonSilvaT/ControleEstoque.git
```


* Crie uma virtualenv dentro do projeto utilizando Python 3

```
cd ControleEstoque
python3 -m venv .venv
```


* Ative o virtualenv

```
source .venv/bin/activate
```


* Atualize o pip

```
pip install --upgrade pip
```


* Instale as dependências

```
pip install -r requirements.txt
```

* Gerar arquivo de configurações do projeto

```
python contrib/env_gen.py
```


* Rode as migrações

```
python manage.py migrate
```

* Rode o servidor django

```
python manage.py runserver
```


## Configuração do Projeto

Este projeto contém duas branches principais

* master

Contém o projeto integrado ao Heroku (em construção)


* local

Contém o projeto para uso local (em construção)


## Principais Tecnologias

Este projeto foi construído utilizando:

* Python 3.8.5
* Django 3.1.1
* Bootstrap 4
* JQuery 3.5.1
* Popper
* PostgreSQL