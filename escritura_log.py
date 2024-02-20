import json
import time
#import datetime import datetime
class EscrituraLog:
    
    def __init__(self):
        pass


def escritura_log2(servio,request,response,tiempo_total):
    
    end_time = datetime.now()
    time_elapsed = end_time - start_time
    fe=end_time.strftime("%Y-%m-%d %H:%M:%S")
    log_data = {"log_data":{"fecha":fe,
            "Level": "INFO",
            "Mensaje": {"Peticion": request, "Respuesta": response},
            "Servicios": [servio],
            "TiempoTotal": tiempo_total }}
    print(log_data)
