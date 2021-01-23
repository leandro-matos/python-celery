# flask_celery

## Pré requisitos

- Python3 instalado
- Git instalado

## Deploy

Para fazer o deploy na sua máquina e utilizar como exemplo, siga o passo a passo a seguir.

- Clone o repositório.

```bash
git clone 
```

- Acesse o diretório

```bash
cd 
```

- Crie uma virtual env

```bash
python3 -m venv .venv
```

- Ative a virtual env

```bash
source .venv/bin/activate
```

- Instale as bibliotecas:

```bash
pip install -r requirements.txt
```

- Executando o gunicorn na porta 5000:

```bash
gunicorn -c setup.py run:app
```

- Executando o celery, necessário iniciar um container do rabbitmq:

```bash
celery --app=app.celery_runner worker --loglevel=info
```

- Rodar via docker:

```bash
docker pull leandromatpereira/flask-with-celery
docker container run --name flask-api -p 5000:5000 -d leandromatpereira/flask-with-celery
```