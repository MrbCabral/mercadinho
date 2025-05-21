# Aula de Django

## Criar ambiente virtual python
```
python -m venv ambiente
```

## Ativar ambiente virtual criado

Linux
```bash
source ambiente/bin/activate
```

Windows
```cmd
ambiente\Scripts\activate
```

## Instalar o Django
```
pip install django
```

## Criar projeto Django
```
django-admin startproject mercadinho
```

## Alterar idioma para Português do Brasil
Abrir o arquivo `settings.py` do projeto criado (`mercadinho/settings.py`) <br>
Alterar a variável `LANGUAGE_CODE` para `pt-br`
```python
LANGUAGE_CODE = "pt-br"
```

## Criar as tabelas padrões do Django
```
python manage.py migrate
```

## Criar o superusuário / root / admin
```
python manage.py createsuperuser
```

## Iniciar o servidor
```
python manage.py runserver
```

## Criar uma aplicação
```
python manage.py startapp estoque
```

