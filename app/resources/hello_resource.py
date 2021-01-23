from flask_restful import Resource
from flask_restful import reqparse
import app.celery_runner

class HelloResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('idade', type=str, required=True, help='O campo idade é obrigatório')
    
    def get(self, name):
        message = f'Hello {name}'
        task = app.celery_runner.hello.delay(message)
        return {"message": 'Aguarde o seu nome será escrito no arquivo file.log'}
    
    def post(self, name):
        data = HelloResource.parser.parse_args()
        idade = data['idade']
        return {"message": f'Olá {name}, você informou que tem {idade} anos'}