import json
import os
import datetime
import time
import psycopg2
from psycopg2 import Error
import boto3
from aws_lambda_powertools.event_handler import LambdaFunctionUrlResolver

class InvocaLambda:
    
    def __init__(self):
        pass

    def invoca_lambda(self,evento):
        #event = "{Evento:GET,healthcheck:true}"
        print('[Comenzando la solicitud] '+json.dumps(str(evento)))
        funcion_name = os.environ['nombre_funcion']
        lambda_client = boto3.client('lambda')
        payload = json.dumps(evento)
        print("Request [url: %s]",funcion_name)
        response = lambda_client.invoke(
               FunctionName = funcion_name,
               Payload = payload
            )
        response_payload = response['Payload'].read()
        return response_payload
        
    def invoca_lambda_resolver
        app = LambdaFunctionUrlResolver()
        @app.get("/todos")
        
    def get_todos():
    todos: Response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos.raise_for_status()

    # for brevity, we'll limit to the first 10 only
    return {"todos": todos.json()[:10]}
    
    