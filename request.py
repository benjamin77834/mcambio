import json
import os
import requests
import re
from datetime import timedelta
from escritura_log import EscrituraLog
import time
import pytz
from datetime import datetime, timedelta

class Solicitud:
    
    def __init__(self):
        pass

    def solicitud_get(self):
        start = time.time()
        headers = {'Content-Type':'application/json'}
        url = os.environ['url_get']
        print("Request [url: %s, header:%s]", url,headers)
        response = requests.get(url=url, params='', headers=headers,timeout=20)
        end = time.time()
        totaltime = end - start
        escribe_log=EscrituraLog()
        escrituralog_unico=escribe_log.escritura_log("GET",response,totaltime)
        print("Esto es el envío de una solicitud GET")

        if response.status_code == 200:
            print('Esta es la respuesta recibida:')
            print(response.text)
            print('También se puede interpretar el json por variables')
            mensaje = response.json()['mensaje']
            folio = response.json()['folio']
            print('Esta es la respuesta mensaje:' +mensaje)
            print('Esta es la respuesta folio:' +folio)
        

        return (response)
    
    