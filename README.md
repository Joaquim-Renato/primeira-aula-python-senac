# Projeto Django Básico

Este é um projeto básico em Python usando o framework Django. Este guia irá orientá-lo nos primeiros passos para configurar e rodar seu projeto Django localmente.

## Pré-requisitos

Certifique-se de ter os seguintes requisitos instalados:

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)
- Virtualenv (opcional, mas recomendado)

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
