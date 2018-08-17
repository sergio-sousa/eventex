
# Eventex

Sistema de Eventos encomendado pela Morena.

## Como desenvolver ?
1. Clone o repositorio.
2. Crie um virtualenv com Python 3.5 
3. Ative o virtualenv.
4. Instale as dependências. 
5. Configure a instância com o .env
6. Execute os teste.
```console
git clone git@github.com.br:henriquebastos/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test

```

## Como fazer o deploy ?
1. Cria uma instância no heroku
2. Envie as configurações para o heroku
3. Defina uma SECREY_KEY segura para a instância.
4. Defina DEBUG=False.
5. Configura o serviço de email.
6. Envio o código para o heroku.
```console
heroku create minhaconta
heroku config:push
heroku config:set SECRET_KEY= `python contrib/secret_gen.py`
# configuro email
git push heroku master --force

```



