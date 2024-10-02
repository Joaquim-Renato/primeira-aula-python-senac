# Projeto Django Básico

Este é um projeto básico em Python usando o framework Django. Este guia irá orientá-lo nos primeiros passos para configurar e rodar seu projeto Django localmente.

## Pré-requisitos

Certifique-se de ter os seguintes requisitos instalados:

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)

## Passos para iniciar

### 1. Verificando a instalação do Python

Verifique se o Python está instalado corretamente em sua máquina:

```bash
python --version

python -m venv nome_do_ambiente
````
## Instale o Django usando o pip:
``` bash
pip install django
```
## Verifique a versão instalada do Django:
``` bash
django-admin --version
```
## Criando um Projeto Django
No diretório onde deseja criar seu projeto, execute:
``` bash
django-admin startproject nome_do_projeto
cd nome_do_projeto
```
## Executando o servidor de desenvolvimento
``` bash
python manage.py runserver
```
## Criando um App Django:
``` bash 
python manage.py startapp nome_do_app
```
----
# Configuração de API Django com MySQL

Este guia descreve os passos necessários para configurar uma API em Django usando o banco de dados MySQL.

## Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado:

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- MySQL Server
- MySQL Client (biblioteca para comunicação com o MySQL)
  
## Passos para configurar Django com MySQL

### 1. Instalar a biblioteca `mysqlclient`

Django requer a biblioteca `mysqlclient` para conectar-se ao MySQL. Instale-a executando o comando:

```bash
pip install mysqlclient
```

2. Configurar o MySQL
Acesse o MySQL com seu usuário administrador:

````bash
mysql -u root -p
````

Crie o banco de dados que será usado pela sua API:

````sql
CREATE DATABASE nome_do_banco;
`````
3. Configurar o arquivo settings.py
No arquivo settings.py do seu projeto Django, configure a conexão com o MySQL. Atualize a seção DATABASES com as suas credenciais:

````python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_banco',   # Nome do banco de dados
        'USER': 'seu_usuario',     # Usuário do MySQL
        'PASSWORD': 'sua_senha',   # Senha do MySQL
        'HOST': 'localhost',       # Endereço do servidor MySQL (localhost para local)
        'PORT': '3306',            # Porta do MySQL (3306 é o padrão)
    }
}
````
4. Aplicar as migrações
Após configurar o MySQL no settings.py, você precisa aplicar as migrações do Django para criar as tabelas iniciais no banco de dados MySQL:

````bash
python manage.py migrate
```` 
