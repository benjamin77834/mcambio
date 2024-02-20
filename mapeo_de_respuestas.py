import json
import time

class MapeoRespuestas:
    
    def __init__(self):
        pass

    def mapeo_respuesta(self,response):
        now = time.ctime()
        
        return {
            'statusCode': 200,  
            'headers': { 
                'Content-Type': 'application/json'
                }, 
            'descripcion': 'Bienvenido a Lambda',
            'body': json.dumps(response)
        }
        
        
    def mapeo_monitoreo_estado(self,health):
    
        return {
            'estatus': health
        }
        
    