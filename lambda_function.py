import json
from request import Solicitud
#from request import EscrituraLog
import requests
from crypto import *
import logging
import time
import pytz
import datetime as datetime
from datetime import datetime
import base64


def lambda_handler(event, context):
    start_time = datetime.now()
    #print("Evento recibido:", json.dumps(event, indent=2))
    raw_path=event['resource']
    method=event['httpMethod']
    yu=event['headers']
    para=event['queryStringParameters']
    xrequest=yu['x-request-id'] if yu.__contains__('x-request-id') else ""
    id_acceso=yu['x-id-acceso'] if yu.__contains__('x-id-acceso') else ""
    #id_acceso=''
    
   
    
    
    
    id_rr5=id_acceso
    iox=''
    payload2=event['body']
    
    xc=str(xrequest)
    xc=xc[:3]
    print(xc)
    if len(xrequest)==15 and (xc=="UID" or xc=="uid" ):
        print("xrequest")

                
    else:
        print("sin xrequest")
        ui={'codigo':'400.Sipa-Sistemas-Negocios-Comsion-Remesas-Mesa-Cambio-Catalogos.4000',
        'mensaje':'Datos de entrada incorrectos, por favor valide su informacion.',
        'folio':xrequest,
        'info':'https://baz-developer.bancoazteca.com.mx/info#400.Sipa-sistemas-Negocios-Comision-Remesas-Mesa-Cambio-Catalogos.4000',
        'detalles':'["Datos de entrada incorrectos - x-id-request es requerido"]'
                }
       # print(ui)
        respuesta = {
        'statusCode': '400',
        'headers': {'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': "*",
        'Access-Control-Allow-Headers': "origin, content-type, accept, authorization,x-request-id,x-id-acceso",
        'Access-Control-Allow-Methods': "GET, POST, PUT, DELETE, OPTIONS, HEAD",
        'Access-Control-Allow-Credentials': True},
        'body':json.dumps(ui)
        
        }
        escritura_log2('LBD_MCAMBIO-PY',json.dumps(event['body']),respuesta,start_time)

        return respuesta    
   
        
    
    
    
    if para:
        #if para['idPais']:
        idPais=para['idPais'] if para.__contains__('idPais') else ""
        
        nombreUsuario=para['nombreUsuario'] if para.__contains__('nombreUsuario') else ""
        idAgente=para['idAgente'] if para.__contains__('idAgente') else ""  
        idModulo=para['idModulo'] if para.__contains__('idModulo') else ""
        
           
    else:
        idPais=''
        nombreUsuario=''
        idModulo=''
        

                
        #return respuesta    
        
        
        

    user = os.environ["akey"]
    password = os.environ["asecret"]
    urlt = os.environ["urlt"]
    alb = os.environ["alb"]
    
   
    userm=str(user)+':'+str(password)

    message_bytes = userm.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    #print(base64_message)

    payload = "grant_type=client_credentials"
   # c =  "https://" + b + ".banco"
    url="https://"+ urlt + "/oauth2/v1/token"
    ui="Basic " + base64_message
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization': ui
              }
    #print(headers)          
   
    try:    
        rr2 = requests.request("POST", url, headers=headers, data=payload,verify=False)
        io2=json.loads(rr2.text)
        #print(io2)     
        acetoken=io2["access_token"];
      
        #print("Token: " +acetoken)
        bea="Bearer " + acetoken
        
        headers2 = {
            "Content-Type": "application/json; charset=UTF-8",
            "x-request-id":xrequest,
            "x-id-acceso":id_acceso,
            "Authorization":bea
    
        }
        
        
        headers29 = {
            "Content-Type": "application/json; charset=UTF-8",
            "x-request-id":xrequest,
  
            "Authorization":bea
    
        }
        headers22 = {
            "Content-Type": "application/json; charset=UTF-8",
            "x-request-id":xrequest,
       
            "Authorization":bea
    
        }
        
        url="https://"+ urlt + "/sipa/seguridad/v1/aplicaciones/llaves"
        rrx = requests.request("GET",url=url,headers=headers22,verify=False)
        print("llaves apigee:")
        print(rrx.text)
        io=json.loads(rrx.text)
        aed = io["resultado"]["accesoSimetrico"]
        haed = io["resultado"]["codigoAutentificacionHash"]   
        aed3=aed
        haed3=haed
        id_acceson = io["resultado"]["idAcceso"]   
        
        print("aed "+aed)
        print("haed "+haed)
                
        
        key_pu = io["resultado"]["accesoPublico"]  
        key_pu1=key_pu
        key_pri = io["resultado"]["accesoPrivado"] 
        
        
        headers24 = {
            "Content-Type": "application/json; charset=UTF-8",
            "x-request-id":xrequest,
            "x-id-acceso":id_acceson,
            "Authorization":bea
    
        }  
        
            
        if  (raw_path=="/numeros-cuenta"  and method=='GET' ) or (method=="POST" and  raw_path=="/historicos-cuenta/busquedas" ) or (method=="POST" and  raw_path=="/acumulados/transacciones/busquedas") or (method=="PUT" and raw_path=="/transacciones/acumulados") or (method=="POST" and  raw_path=="/remesas/cotizaciones") :
            
            
            
          
            
            if len(str(id_acceso))==15:
                print("id_acceso:",id_acceso)
               
                headers={"x-request-id":xrequest}
                url=alb+":8102/sipa-sistemas-negocios-comision-seguridad-v1/aplicaciones/llaves/"+id_acceso
                print("url:"+url+"headers:"+str(headers))
                rrx = requests.request("GET",url=url,headers=headers,verify=False)
                print("llaves sime")

                
                if str(rrx.status_code)!='200': 
                    print("llave invalidada")
                    ui={'codigo':'400.Sipa-Sistemas-Negocios-Comsion-Remesas-Mesa-Cambio-Catalogos.4000',
                    'mensaje':'Datos de entrada incorrectos, por favor valide su informacion.',
                    'folio':xrequest,
                    'info':'https://baz-developer.bancoazteca.com.mx/info#400.Sipa-sistemas-Negocios-Comision-Remesas-Mesa-Cambio-Catalogos.4000',
                   'detalles':'["Datos de entrada incorrectos - x-id-acceso es requerido"]'
                    }
                    respuesta = {
            'statusCode': '400',
            'headers': {'Content-Type': 'application/json',
                  'Access-Control-Allow-Origin': "*",
        'Access-Control-Allow-Headers': "origin, content-type, accept, authorization,x-request-id,x-id-acceso",
                'Access-Control-Allow-Methods': "GET, POST, PUT, DELETE, OPTIONS, HEAD",
                'Access-Control-Allow-Credentials': True},
            'body':json.dumps(ui)
            
                }
                    #print(ui)
                    escritura_log2('LBD_MCAMBIO-PY',event['body'],ui,start_time)
    
                    return respuesta    
                else:
                    io=json.loads(rrx.text)
                    aed = io["resultado"]["accesoSimetrico"]
                    haed = io["resultado"]["codigoAutentificacionHash"]  
                    aed2=aed
                    haed2=haed
                    print("aed2: ",aed2)
                    print("haed2: ",haed)

                
            else:
                print("sin id")
                ui={'codigo':'400.Sipa-Sistemas-Negocios-Comsion-Remesas-Mesa-Cambio-Catalogos.4000',
                'mensaje':'Datos de entrada incorrectos, por favor valide su informacion.',
                'folio':xrequest,
                'info':'https://baz-developer.bancoazteca.com.mx/info#400.Sipa-sistemas-Negocios-Comision-Remesas-Mesa-Cambio-Catalogos.4000',
               'detalles':'["Datos de entrada incorrectos - x-id-acceso es requerido"]'
                }
                respuesta = {
        'statusCode': '400',
        'headers': {'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': "*",
    'Access-Control-Allow-Headers': "origin, content-type, accept, authorization,x-request-id,x-id-acceso",
            'Access-Control-Allow-Methods': "GET, POST, PUT, DELETE, OPTIONS, HEAD",
            'Access-Control-Allow-Credentials': True},
        'body':json.dumps(ui)
        
            }
                #print(ui)
                
                
                escritura_log2('LBD_MCAMBIO-PY',event['body'],ui,start_time)

                return respuesta    

                

                

            
        
        print("key_pu: "+key_pu)
        headers24 = {
            "Content-Type": "application/json; charset=UTF-8",
            "x-request-id":xrequest,
            "x-id-acceso":id_acceson,
            "Authorization":bea
    
        }   
            

        if raw_path=="/paises" and method=='GET':     
            if idPais:
                url5="https://"+urlt+"/sipa/sistemas-negocios-comision/remesas/mesa-cambio/catalogos/v1/paises?idPais="+idPais
            else:
                url5="https://"+urlt+"/sipa/sistemas-negocios-comision/remesas/mesa-cambio/catalogos/v1/paises"
         
        if raw_path=="/paises/detalles" and method=='GET':
            print("nombreUsuario>",nombreUsuario)

            url5="https://"+urlt+"/sipa/sistemas-negocios-comision/remesas/mesa-cambio/catalogos/v1/paises/detalles?idPais="+idPais+"&nombreUsuario="+nombreUsuario

                
            
            
                   
        if  raw_path=="/agentes" and method=='GET':
           
            url5="https://"+urlt+"/sipa/sistemas-negocios-comision/remesas/mesa-cambio/catalogos/v1/agentes?idPais="+idPais
           # print(idPais,url5)
                

            
        if  raw_path=="/divisas" and method=='GET':   
            #print(idPais)
            #if idPais:
            #    url5="https://dev-api.bancoazteca.com.mx:8080/sipa/sistemas-negocios-comision/remesas/mesa-cambio/catalogos/v1/divisas?idPais="+idPais  
            #    print(idPais,url5)   
            url5="https://"+urlt+"/sipa/sistemas-negocios-comision/remesas/mesa-cambio/catalogos/v1/divisas?idPais="+idPais  

        if  raw_path=="/numero-cuenta"  and method=='GET':   
            url5="https://"+urlt+"/sipa/sistemas-negocios-comision/remesas/mesa-cambio/catalogos/v1/numeros-cuenta"  
            print(url5)
            headers2=headers24
                
            
        if  raw_path=="/numeros-cuenta"  and method=='GET':   
                
                if id_acceso:
                    url5="https://"+urlt+"/sipa/sistemas-negocios-comision/remesas/mesa-cambio/catalogos/v1/numeros-cuenta"  
                    print(url5)    
                    headers2=headers24
                else:
                    ui={'codigo':'400.Sipa-Sistemas-Negocios-Comsion-Remesas-Mesa-Cambio-Catalogos.4000',
                    'mensaje':'Datos de entrada incorrectos, por favor valide su informacion.',
                    'folio':xrequest,
                    'info':'https://baz-developer.bancoazteca.com.mx/info#400.Sipa-sistemas-Negocios-Comision-Remesas-Mesa-Cambio-Catalogos.4000',
                    'detalles':'["Datos de entrada incorrectos - x-id-acceso es requerido"]'
                    }
                    ui=json.dumps(ui)
                    print(ui)
                    
                
                    respuesta = {
        'statusCode': '400',
        'headers': {'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': "*",
    'Access-Control-Allow-Headers': "origin, content-type, accept, authorization,x-request-id,x-id-acceso",
            'Access-Control-Allow-Methods': "GET, POST, PUT, DELETE, OPTIONS, HEAD",
            'Access-Control-Allow-Credentials': True},
        'body':ui
        
            }
                    escritura_log2('LBD_MCAMBIO-PY',json.dumps(event['body']),respuesta,start_time)

                    return respuesta    
            
            
           
            
        if  raw_path=="/eventos" and method=='GET':   
    
            url5="https://"+urlt+"/sipa/sistemas-negocios-comision/remesas/mesa-cambio/catalogos/v1/eventos?idModulo="+idModulo  
            print(url5,"eventos->")           
                    
            
        
        if raw_path=="/mesa-cambio" and method=='GET':     
            url5="https://"+urlt+"/sipa/sistemas-negocios-comision/remesas/mesa-cambio/catalogos/v1/mesa-cambio"    
       
          
        if raw_path=="/estados" and method=='GET':   
          #  https://api.dev-remesas-baz.com.mx/sipa/sistemas-negocios-comision/remesas/mesa-cambio/catalogos/v1/estados
            url5="https://"+urlt+"/sipa/sistemas-negocios-comision/remesas/mesa-cambio/catalogos/v1/estados?idPais="+idPais    
   
        if raw_path=="/subsidiarias" and method=='GET':     
            url5="https://"+urlt+"/sipa/sistemas-negocios-comision/remesas/mesa-cambio/catalogos/v1/subsidiarias?idPais="+idPais+"&idAgente="+idAgente    
       
       
        if method=="GET":

            print("headers")
            print(headers2)
            print("url5: ",url5)
            rr = requests.request("GET",url=url5,headers=headers2,verify=False)
            sta_code=rr.status_code
        
            #print(rr.text)
        if  raw_path=="/numeros-cuenta"  and method=='GET':  
            print("por aqui--->>>>")
            ui=json.dumps(rr.text)
            ui=json.loads(rr.text)
            print(ui)
        
            # event3=json.loads(rr)
            event4=ui['resultado']['cuentas']
            fo=ui['folio']
            cod=ui['codigo']
            mens=ui['mensaje']
            print(key_pri)
            uif=''
            for eve in event4:

                    das=eve['numero']
                    print("numero en rsacifrado:")
                    print(das)
                    cifra=descifrar_datosRSA2(str(das),key_pri)
                    print("descrsa:")
                    print(cifra)
                    cifra=aes_ec(cifra,aed,haed)
                    uif+="{'numero':'"+cifra+"'},"
                    print("aes:")
                    print(cifra)
            
            uif=uif[:-1]

            
            ui={'codigo':cod,'mensaje':mens,
          #  "x-id-acceso":id_acceson,
            'folio':fo,'resultado':{'cuentas':[uif]}}
            ui=json.dumps(ui)
            print(ui)
            #uift = str(ui).replace('"',"")
            print("####")
            print(ui)

            
            #uop=rsa_encryptui("hola")
        #    print("encruss---")
           # print(uop)
           
           
           
           
        ###########   
           
            respuesta = {
        'statusCode': sta_code,
        'headers': {'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': "*",
            'Access-Control-Allow-Headers': "origin, content-type, accept, authorization,x-request-id,x-id-acceso",
            'Access-Control-Allow-Methods': "GET, POST, PUT, DELETE, OPTIONS, HEAD",
            'Access-Control-Allow-Credentials': True},
        'body':ui
        
            }
         #   print("cifradosss:--->")
        #    print(respuesta)
            escritura_log2('LBD_MCAMBIO-PY',ui,respuesta,start_time)

            return respuesta

        
        #####################    
            
        if method=="POST" and  raw_path=="/tipos-cambio/busquedas" :
            url5="https://"+urlt+"/sipa/sistemas-negocios-comision/remesas/mesa-cambio/catalogos/v1/tipos-cambio/busquedas"
            payload=event["body"]
            print("inicio body")
          #  print(payload)
            print("fin body")    
            
            
        if method=="POST" and  raw_path=="/acumulados/paises/busquedas" :
        
            if xrequest:
                url5="https://"+urlt+"/sipa/sistemas-negocios-comision/remesas/mesa-cambio/catalogos/v1/acumulados/paises/busquedas"
                payload=event["body"]
                print("inicio body")
                print(payload)
                print("fin body")
            else:
                ui={'codigo':'400.Sipa-Sistemas-Negocios-Comsion-Remesas-Mesa-Cambio-Catalogos.4000',
                    'mensaje':'Datos de entrada incorrectos, por favor valide su informacion.',
                    'folio':xrequest,
                    'info':'https://baz-developer.bancoazteca.com.mx/info#400.Sipa-sistemas-Negocios-Comision-Remesas-Mesa-Cambio-Catalogos.4000',
                    'detalles':'["Datos de entrada incorrectos - x-request-id es requerido"]'
                    }
                ui=json.dumps(ui)
                print(ui)
                
                respuesta = {
        'statusCode': '400',
        'headers': {'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': "*",
    'Access-Control-Allow-Headers': "origin, content-type, accept, authorization,x-request-id,x-id-acceso",
            'Access-Control-Allow-Methods': "GET, POST, PUT, DELETE, OPTIONS, HEAD",
            'Access-Control-Allow-Credentials': True},
        'body':ui
        
            }
                escritura_log2('LBD_MCAMBIO-PY',json.dumps(payload),respuesta,start_time)
                return respuesta    
            

            
        if method=="POST" and  raw_path=="/acumulados/transacciones/busquedas" :
            if id_acceso:
                print("id_acceso:"+id_acceso)
                
            
                print("trae id_accce: "+id_rr5)
                url5="https://"+urlt+"/sipa/sistemas-negocios-comision/remesas/mesa-cambio/catalogos/v1/acumulados/transacciones/busquedas"
                payload=event["body"]
                print("inicio body amul")
                print(payload)
                print("fin body")  
                    #print("headers2")
                    #print(json.loads(headers2))
                headers2=headers24
                print(url5)
            else:
                ui={'codigo':'400.Sipa-Sistemas-Negocios-Comsion-Remesas-Mesa-Cambio-Catalogos.4000',
                'mensaje':'Datos de entrada incorrectos, por favor valide su informacion.',
                'folio':xrequest,
                'info':'https://baz-developer.bancoazteca.com.mx/info#400.Sipa-sistemas-Negocios-Comision-Remesas-Mesa-Cambio-Catalogos.4000',
                'detalles':'["Datos de entrada incorrectos - x-id-acceso es requerido"]'
                }
                ui=json.dumps(ui)
                print(ui)
                
                
                respuesta = {
        'statusCode': '400',
        'headers': {'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': "*",
    'Access-Control-Allow-Headers': "origin, content-type, accept, authorization,x-request-id,x-id-acceso",
            'Access-Control-Allow-Methods': "GET, POST, PUT, DELETE, OPTIONS, HEAD",
            'Access-Control-Allow-Credentials': True},
        'body':ui
        
            }
                escritura_log2('LBD_MCAMBIO-PY',json.dumps(payload),respuesta,start_time)

                return respuesta    
            

                    
        if method=="POST" and  raw_path=="/historicos-cuenta/busquedas" :
            
  
            
            
            url5="https://"+urlt+"/sipa/sistemas-negocios-comision/remesas/mesa-cambio/catalogos/v1/historicos-cuenta/busquedas"
            headers2=headers24
           
            pay=json.loads(payload2)
            cuenta=pay['numeroCuenta'] if pay.__contains__('numeroCuenta') else ""
            
            if len(str(cuenta))<15:

                uix={'codigo':'400.Sipa-Sistemas-Negocios-Comsion-Remesas-Mesa-Cambio-Catalogos.4000',
                'mensaje':'Datos de entrada incorrectos, por favor valide su informacion.',
                'folio':xrequest,
                'info':'https://baz-developer.bancoazteca.com.mx/info#400.Sipa-sistemas-Negocios-Comision-Remesas-Mesa-Cambio-Catalogos.4000',
                'detalles':'["Datos de entrada incorrectos - numeroCuenta  no tiene el valor o cifrado en AES"]'
                }
                uix=json.dumps(uix)
                print(uix)
                respuesta = {
        'statusCode': '400',
        'headers': {'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': "*",
    'Access-Control-Allow-Headers': "origin, content-type, accept, authorization,x-request-id,x-id-acceso",
            'Access-Control-Allow-Methods': "GET, POST, PUT, DELETE, OPTIONS, HEAD",
            'Access-Control-Allow-Credentials': True},
        'body':uix
        
            }
                
                escritura_log2('LBD_MCAMBIO-PY',json.loads(payload2),respuesta,start_time)
                return respuesta    
            
            
            
            print("cuenta:"+cuenta)
            cuenta=aes_gcm_decrypt(cuenta,aed,haed)
            print("cuenta:"+cuenta)
            fechaFinal=pay['fechaFinal'] if pay.__contains__('fechaFinal') else ""
            fechaInicial=pay['fechaInicial'] if pay.__contains__('fechaInicial') else ""
            nombreUsuario=pay['nombreUsuario'] if pay.__contains__('nombreUsuario') else ""
            cuenta=cifrar_datosRSA2(cuenta,key_pu)
            print("cuenta: "+cuenta)
            #payload2.update({"nuemroCuenta":cuenta})
            #  'nuemroCuenta':cuenta,
            pay2={
                'fechaFinal':fechaFinal,
                'fechaInicial':fechaInicial,
                'cuenta':cuenta,
                'nombreUsuario':nombreUsuario
            }
            headers2=headers24
            #print("cuenta:"+cuenta)
            print("inicio body")
            print(pay2)
            print("fin body")  
            payload=json.dumps(pay2)
            print(payload)
            
            

            
            
        if method=="POST" and  raw_path=="/transacciones-bloqueadas/busquedas":
            url5="https://"+urlt+"/sipa/sistemas-negocios-comision/remesas/mesa-cambio/catalogos/v1/transacciones-bloqueadas/busquedas"
            payload=event["body"]
            #nombreUsuario=payload['nombreUsuario'] if payload.__contains__('nombreUsuario') else ""
            #url='http://internal-ALB-FARGATE-REMESAS-DEV-300173178.us-east-1.elb.amazonaws.com:8102/sipa-sistemas-negocios-comision-seguridad-v1/aplicaciones/llaves/'+id_acceso
            #rr = requests.request("GET",headers=headers2,url=url)
            #io=json.loads(rr.text)
            #aed = io["resultado"]["accesoSimetrico"]
            #haed = io["resultado"]["codigoAutentificacionHash"]
            #nombreUsuario2=cifrar_datosRSA(nombreUsuario,'')
            #nombreUsuario2=descifrar_aes_gcm(nombreUsuario, aed, haed)
            #payload.update({"nombreUsuario":nombreUsuario2})
            #headers2=headers24
            
            
            print("inicio body")
            print(payload)
            print("fin body")        
            
            
        if method=="POST" and  raw_path=="/remesas/cotizaciones" :
            print(raw_path)
            url5="https://"+urlt+"/sipa/sistemas-negocios-comision/remesas/gestion-mesa-cambio/v1/remesas/cotizaciones"
            payload=event["body"]
            #print(payload)
            #ui=json.dumps(rr.text)
            ui=json.loads(payload)
            #print(ui)
            
           # das2=event["body"]["envios"]
            uix=ui['envios'] if ui.__contains__('envios') else ""
            origen=ui['origen'] if ui.__contains__('origen') else ""
            destino=ui['destino'] if ui.__contains__('destino') else ""
            detalle=ui['detalle'] if ui.__contains__('detalle') else ""
            #print("antesextra")
            datosExtra=ui['datosExtra'] if ui.__contains__('datosExtra') else ""
            print(datosExtra)
            
            numeroCliente=uix['numeroCliente'] if uix.__contains__('numeroCliente') else ""

            if len(str(numeroCliente))<15:

                uix={'codigo':'400.Sipa-Sistemas-Negocios-Comsion-Remesas-Mesa-Cambio-Catalogos.4000',
                'mensaje':'Datos de entrada incorrectos, por favor valide su informacion.',
                'folio':xrequest,
                'info':'https://baz-developer.bancoazteca.com.mx/info#400.Sipa-sistemas-Negocios-Comision-Remesas-Mesa-Cambio-Catalogos.4000',
                'detalles':'["Datos de entrada incorrectos - numeroCliente  no tiene el valor o cifrado en AES"]'
                }
                uix=json.dumps(uix)
                print(uix)
                respuesta = {
        'statusCode': '400',
        'headers': {'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': "*",
    'Access-Control-Allow-Headers': "origin, content-type, accept, authorization,x-request-id,x-id-acceso",
            'Access-Control-Allow-Methods': "GET, POST, PUT, DELETE, OPTIONS, HEAD",
            'Access-Control-Allow-Credentials': True},
        'body':uix
        
            }
                
                escritura_log2('LBD_MCAMBIO-PY',json.loads(payload2),respuesta,start_time)
                return respuesta    


            if datosExtra:
              #  print("hola")
                #uify=[]
                verf=verifica_valor2(datosExtra)
                print("verificaicon:",verf)
                if verf=='ok':
                    datosExtra=actualizar_valor2(datosExtra,"identificador",key_pu,aed,haed)
                    print("datosExtra: ", datosExtra) 
                else:
                    
                            
                    uix={'codigo':'400.Sipa-Sistemas-Negocios-Comsion-Remesas-Mesa-Cambio-Catalogos.4000',
                'mensaje':'Datos de entrada incorrectos, por favor valide su informacion.',
                'folio':xrequest,
                'info':'https://baz-developer.bancoazteca.com.mx/info#400.Sipa-sistemas-Negocios-Comision-Remesas-Mesa-Cambio-Catalogos.4000',
                'detalles':'["Datos de entrada incorrectos - Datosextra no tiene el valor o cifrado en AES"]'
                }
                    uix=json.dumps(uix)
                    print(uix)
                
                
                    respuesta = {
        'statusCode': '400',
        'headers': {'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': "*",
    'Access-Control-Allow-Headers': "origin, content-type, accept, authorization,x-request-id,x-id-acceso",
            'Access-Control-Allow-Methods': "GET, POST, PUT, DELETE, OPTIONS, HEAD",
            'Access-Control-Allow-Credentials': True},
        'body':uix
        
            }
                    escritura_log2('LBD_MCAMBIO-PY',json.loads(payload2),respuesta,start_time)

                    return respuesta    
            #datosExtra=[]        
           # print("cuenta:"+numeroCliente)
        #    print("acuenta:>"+aed2)
            #print("hcuenta:"+haed2)
            cuenta=aes_gcm_decrypt(numeroCliente,aed,haed)
            
         #   print("cuenta desaes:"+cuenta)
            das=cifrar_datosRSA2(cuenta,key_pu)
            uix.update({"numeroCliente":das})
            print(uix)
            uif={'origen':origen,'destino':destino,'envios':uix,'detalle':detalle,'datosExtra':datosExtra}
            print("final:")
           # print(uif)
            payload=uif
            
            
            print("inicio body")
            print(json.dumps(payload))
            print("fin body")
            print("headers de envio:")
            print(headers24)
            
            payload2=json.dumps(payload)
            rr = requests.post(url=url5,headers=headers24,data=payload2,verify=False)
            sta_code=rr.status_code
            print("#######...POST General..."+raw_path)
            print(rr.text)
            print(sta_code)
            print("raw_path>out>"+raw_path)    
            respuesta = {
        'statusCode': sta_code,
        'headers': {'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': "*",
    'Access-Control-Allow-Headers': "origin, content-type, accept, authorization,x-request-id,x-id-acceso",
            'Access-Control-Allow-Methods': "GET, POST, PUT, DELETE, OPTIONS, HEAD",
            'Access-Control-Allow-Credentials': True},
        'body':rr.text
        
            }
            
   

            escritura_log2('LBD_MCAMBIO-PY',json.loads(payload2),respuesta,start_time)
            return respuesta
            
            
            
        if method=="POST":    
  
            print("headers de envio:")
            print(headers2)
            rr = requests.post(url=url5,headers=headers2,data=payload,verify=False)
            sta_code=rr.status_code
            print("#######...POST General..."+raw_path)
            print(rr.text)
            print(sta_code)
            print("raw_path>out>"+raw_path)    
            
            if method=="POST" and  raw_path=="/historicos-cuenta/busquedas":
                #event3=json.loads(rr)
                print("raw_path historicos: "+str(raw_path))  
                
                print(sta_code)  
                if str(sta_code)=="200":
                  #  print("200")
                    respuesta = {
        'statusCode': sta_code,
        'headers': {'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': "*",
    'Access-Control-Allow-Headers': "origin, content-type, accept, authorization,x-request-id,x-id-acceso",
            'Access-Control-Allow-Methods': "GET, POST, PUT, DELETE, OPTIONS, HEAD",
            'Access-Control-Allow-Credentials': True},
        'body':rr.text
        
            }
                    escritura_log2('LBD_MCAMBIO-PY',json.dumps(payload),respuesta,start_time)

                    return respuesta
                else:
                   # print(sta_code)
                    respuesta = {
        'statusCode': sta_code,
        'headers': {'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': "*",
            'Access-Control-Allow-Headers': "origin, content-type, accept, authorization,x-request-id,x-id-acceso",
            'Access-Control-Allow-Methods': "GET, POST, PUT, DELETE, OPTIONS, HEAD",
            'Access-Control-Allow-Credentials': True},
        'body':rr.text
        
                }
                
                    escritura_log2('LBD_MCAMBIO-PY',json.dumps(payload),respuesta,start_time)

                    return respuesta
            
                
                
                print("por aqui--->>>>")
                ui=json.dumps(rr.text)
                ui=json.loads(rr.text)
               # print(ui)
            
                # event3=json.loads(rr)
                event4=ui['resultado']['beneficiario']
                fo=ui['folio']
                cod=ui['codigo']
                mens=ui['mensaje']
                
                historicos=ui['historicos']
                uif=''
                for eve in event4:
                        montoActual=eve['montoActual']
                        primerNombre=eve['primerNombre']
                        segundoNombre=eve['segundoNombre']
                        apellidoPaterno=eve['apellidoPaterno']
                        apellidoMaterno=eve['apellidoMaterno']
                        
                        primerNombre=descifrar_datosRSA2(str(primerNombre),key_pri)
                        segundoNombre=descifrar_datosRSA2(str(segundoNombre),key_pri)
                        apellidoMaterno=descifrar_datosRSA2(str(apellidoMaterno),key_pri)
                        apellidoPaterno=descifrar_datosRSA2(str(apellidoPaterno),key_pri)
                        
                        primerNombre=aes_ec(primerNombre,aed,haed)
                        segundoNombre=aes_ec(segundoNombre,aed,haed)
                        apellidoMaterno=aes_ec(apellidoMaterno,aed,haed)
                        apellidoPaterno=aes_ec(apellidoPaterno,aed,haed)
                        uif+="{'primerNombre':'"+primerNombre+"','segundoNombre':'"+segundoNombre+"'apellidoMaterno':'"+apellidoMaterno+"','apellidoPaterno':"+apellidoPaterno+"',}"
            
                uif=uif[:-1]

            
                ui={'codigo':cod,'mensaje':mens,'folio':fo,'resultado':{'montoActual':montoActual,'beneficiario':[uif]}}
                ui=json.dumps(ui)
                print(ui)
                #uift = str(ui).replace('"',"")
                print("####")
                print(ui)
                            
                
                respuesta = {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': "*",
     'Access-Control-Allow-Headers': "origin, content-type, accept, authorization,x-request-id,x-id-acceso",
            'Access-Control-Allow-Methods': "GET, POST, PUT, DELETE, OPTIONS, HEAD",
            'Access-Control-Allow-Credentials': True},
        'body':event3
        
            }
    
 
            print("raw_path"+raw_path)
            
            
            if method=="POST" and  raw_path=="/acumulados/paises/busquedas" :

               
                respuesta = {
        'statusCode': sta_code,
        'headers': {'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': "*",
            'Access-Control-Allow-Headers': "origin, content-type, accept, authorization,x-request-id,x-id-acceso",
            'Access-Control-Allow-Methods': "GET, POST, PUT, DELETE, OPTIONS, HEAD",
            'Access-Control-Allow-Credentials': True},
        'body':rr.text
        
                }
               
                    
                    
                
                escritura_log2('LBD_MCAMBIO-PY',json.dumps(payload2),respuesta,start_time)

                return respuesta


            
            
            if method=="POST" and  raw_path=="/acumulados/transacciones/busquedas" :
                print("transacciones:")


                if str(sta_code)!="200":
                   # print(sta_code)
                    respuesta = {
        'statusCode': sta_code,
        'headers': {'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': "*",
            'Access-Control-Allow-Headers': "origin, content-type, accept, authorization,x-request-id,x-id-acceso",
            'Access-Control-Allow-Methods': "GET, POST, PUT, DELETE, OPTIONS, HEAD",
            'Access-Control-Allow-Credentials': True},
        'body':rr.text
        
                }
                    #print(respuesta)
                    
                    escritura_log2('LBD_MCAMBIO-PY',json.dumps(payload2),respuesta,start_time)

                    return respuesta


                ui=json.dumps(rr.text)
                ui=json.loads(rr.text)

                event4=ui['resultado']['acumulados']
                fo=ui['folio']
                cod=ui['codigo']
                mens=ui['mensaje']
    
                uif=''
                uify=[]
                for eve in event4:
    
    
    
                        das=eve['idOrdenPago']
                        paisOrigen=eve['paisOrigen']
                        fechaOperacion=eve['fechaOperacion']
                        idPaisDestino=eve['idPaisDestino']
                        paisDestino=eve['paisDestino']
                        divisaOrigen=eve['divisaOrigen']
                        tipoCambioOrigen=eve['tipoCambioOrigen']
                        montoEnvioDolares=eve['montoEnvioDolares']
                        tipoCambioEnvio=eve['tipoCambioEnvio']
                        divisaDestino=eve['divisaDestino']
                        fechaCompra=eve['fechaCompra']
                        compraTipoCambioDolares=eve['compraTipoCambioDolares']
                        gananciaPerdidaCompra=eve['gananciaPerdidaCompra']
                        fechaVenta=eve['fechaVenta']
                        ventaTipoCambioDolares=eve['ventaTipoCambioDolares']
                        gananciaPerdidaVenta=eve['gananciaPerdidaVenta']
                        #print("idorden:")
                       
                        cifra=descifrar_datosRSA2(str(das),key_pri)
                        cifra=aes_ec(cifra,aed2,haed2)
                        uif+="{'idOrdenPago':'"+cifra+"','paisOrigen':'"+paisOrigen+"','fechaOperacion':'"+fechaOperacion+"','idPaisDestino':"+idPaisDestino+"','paisDestino':"+paisDestino+",'divisaOrigen':'"+divisaOrigen+"','tipoCambioOrigen':"+tipoCambioOrigen+"','montoEnvioDolares':'"+montoEnvioDolares+"','tipoCambioEnvio':'"+tipoCambioEnvio+"','divisaDestino':'"+divisaDestino+"','fechaCompra':'"+str(fechaCompra)+"','compraTipoCambioDolares':'"+str(compraTipoCambioDolares)+"','gananciaPerdidaCompra':'"+str(gananciaPerdidaCompra)+"','fechaVenta':'"+str(fechaVenta)+"','ventaTipoCambioDolares':'"+str(ventaTipoCambioDolares)+"','gananciaPerdidaVenta':'"+str(gananciaPerdidaVenta)+"'},"
                        uifq={'idOrdenPago':cifra,'paisOrigen':paisOrigen,'fechaOperacion':fechaOperacion,
                        'idPaisDestino':idPaisDestino,'paisDestino':paisDestino,'divisaOrigen':divisaOrigen,
                        'tipoCambioOrigen':tipoCambioOrigen,'montoEnvioDolares':montoEnvioDolares,
                        'tipoCambioEnvio':tipoCambioEnvio,'divisaDestino':divisaDestino,
                        'fechaCompra':str(fechaCompra),'compraTipoCambioDolares':str(compraTipoCambioDolares),
                        'gananciaPerdidaCompra':gananciaPerdidaCompra,'fechaVenta':str(fechaVenta),
                        'ventaTipoCambioDolares':ventaTipoCambioDolares,'gananciaPerdidaVenta':str(gananciaPerdidaVenta)
                            
                        }
                        uify.append(uifq)

                uix={'codigo':cod,'mensaje':mens,'folio':fo,'resultado':{'acumulados':uify}}
               
                
                #ui=json.dumps(ui)
               # print(ui)
                #uift = str(ui).replace('"',"")
                #print("####>")
                #print(json.dumps(uix))
    
                
                #uop=rsa_encryptui("hola")
            #    print("encruss---")
               # print(uop)
                respuesta = {
            'statusCode': sta_code,
        'headers': {'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': "*",
            'Access-Control-Allow-Headers': "origin, content-type, accept, authorization,x-request-id,x-id-acceso",
            'Access-Control-Allow-Methods': "GET, POST, PUT, DELETE, OPTIONS, HEAD",
            'Access-Control-Allow-Credentials': True},
            'body':json.dumps(uix)
            
                }
                print("cifradosss:--->")
                print(respuesta)
                escritura_log2('LBD_MCAMBIO-PY',json.dumps(payload2),respuesta,start_time)

                return respuesta

            
            
        if method=="PUT" and  raw_path=="/transacciones/acumulados" :
            url5="https://"+urlt+"/sipa/sistemas-negocios-comision/remesas/gestion-mesa-cambio/v1/transacciones/acumulados"
            das2=json.loads(event['body'])
            
            print("antes de cifrar:")
            print(das2)
            
            idOrdenPago=das2['idOrdenPago'] if das2.__contains__('idOrdenPago') else ""

            
            #das=das2['idOrdenPago']
            #print("idOrdenPago",das)
            
            print("cuenta:"+idOrdenPago)
            print("acuenta:"+aed2)
            print("hcuenta:"+haed2)
            #cuenta=aes_gcm_decrypt(cuenta,aed,haed)
            cuenta=aes_gcm_decrypt(idOrdenPago,aed,haed)
            #cuenta="91tJYSeaXq5x344wEiAunpkXFtt2gduBCaVTS1CWsmYoSGMntxDX"
            print("cuenta desaes:"+cuenta)
            das=cuenta
            #print("idOrdenPago",cuenta)

            #print("aes:",das)
            print("llave_pr:")
            print(key_pri)
            print("llave pub:")
            print(key_pu)
        
            das=cifrar_datosRSA2(str(cuenta),key_pu)
            #des=descifrar_datosRSA2(das,key_pri)
            
            #das=cifrar_datosRSA3(das,key_priv)
            
            print("rsa:",das)
            #print("rsade:",des)
            
            #print("rsapriv:",key_pri)
            das2.update({"idOrdenPago":das})
            payload=das2
        
            print("inicio body")
            print(payload)
            print("fin body")
                


            print("pruebas->>")
            print(payload)
            
            payload2=json.dumps(payload)
            response = requests.request("PUT", url5, headers=headers24, data=payload2,verify=False)

            print(response.text)
            
            
            sta_code=response.status_code
            print("response:")
            print(response.text)
            print("aplicar metodo :" +method)
            print(sta_code)
            
            respuesta = {
        'statusCode': sta_code,
        'headers': {'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': "*",
            'Access-Control-Allow-Headers': "origin, content-type, accept, authorization,x-request-id,x-id-acceso",
            'Access-Control-Allow-Methods': "GET, POST, PUT, DELETE, OPTIONS, HEAD",
            'Access-Control-Allow-Credentials': True},
        'body':response.text
        
            
        
                }
            escritura_log2('LBD_MCAMBIO-PY',payload2,respuesta,start_time)
    
            return respuesta
            
        if method=="PUT" and  raw_path=="/tipo-cambio" :
            url5="https://"+urlt+"/sipa/sistemas-negocios-comision/remesas/gestion-mesa-cambio/v1/tipo-cambio"
            payload=event["body"]
            print("inicio body")
            print(payload)
            print("fin body")    
        
        if method=="PUT" and  raw_path=="/tipo-cambio/ganancia-cambiaria" :
            url5="https://"+urlt+"/sipa/sistemas-negocios-comision/remesas/gestion-mesa-cambio/v1/tipo-cambio/ganancia-cambiaria"
            payload=event["body"]
            print("inicio body")
            print(payload)
            print("fin body")   
        
        
        if method=="PUT":
            
            rr = requests.request("PUT",url=url5,headers=headers24,data=payload,verify=False)
            print("url:")
            print(url5)
            print("headers")
            print(headers24)
            print(rr.text)
            sta_code=rr.status_code
            print("response:")
            print(rr.text)
            print("aplicar metodo :" +method)
            print(sta_code)
            
            if str(sta_code)!="200":
                   # print(sta_code)
                    respuesta = {
        'statusCode': sta_code,
        'headers': {'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': "*",
            'Access-Control-Allow-Headers': "origin, content-type, accept, authorization,x-request-id,x-id-acceso",
            'Access-Control-Allow-Methods': "GET, POST, PUT, DELETE, OPTIONS, HEAD",
            'Access-Control-Allow-Credentials': True},
        'body':rr.text
        
            
        
                }
                
            else:
                   # print(sta_code)
                    respuesta = {
        'statusCode': sta_code,
        'headers': {'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': "*",
            'Access-Control-Allow-Headers': "origin, content-type, accept, authorization,x-request-id,x-id-acceso",
            'Access-Control-Allow-Methods': "GET, POST, PUT, DELETE, OPTIONS, HEAD",
            'Access-Control-Allow-Credentials': True},
        'body':rr.text
        
                }
            
            
            
            
            escritura_log2('LBD_MCAMBIO-PY',json.dumps(payload),respuesta,start_time)
    
            return respuesta
            
            
            
            
     #   if method=="POST":
            
    #        rr = requests.request("POST",url=url5,headers=headers2,data=json.dumps(payload),verify=False)
       #     print("aplicar metodo :" +method)
        
        if len(iox):
            print(iox)
        else:    
            iox=json.loads(rr.text)
        
        print("response:")
        print(iox)
        
        
       
        respuesta = {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': "*",
            'Access-Control-Allow-Headers': "origin, content-type, accept, authorization,x-request-id,x-id-acceso",
            'Access-Control-Allow-Methods': "GET, POST, PUT, DELETE, OPTIONS, HEAD",
            'Access-Control-Allow-Credentials': True},
        'body':json.dumps(iox)
        
            }
        escritura_log2('LBD_MCAMBIO-PY',json.dumps(event['body']),respuesta,start_time)

        return respuesta

           
    except Exception as e:
        print(f"Error al obtener la información de acceso: {str(e)}")

        respuesta = {
        'statusCode': 400,
        'headers': {'Content-Type': 'application/json'},
        'body':json.dumps(str(e))
        
            }
        escritura_log2('LBD_MCAMBIO-PY',json.dumps(event['body']),respuesta,start_time)

        return respuesta
        
              

        
    if id_acceso:
        if ban==5:
            idOrdenPago=event3['idOrdenPago'] if event3.__contains__('idOrdenPago') else ""
        url='http://internal-ALB-FARGATE-REMESAS-DEV-300173178.us-east-1.elb.amazonaws.com:8102/sipa-sistemas-negocios-comision-seguridad-v1/aplicaciones/llaves/'+id_acceso
        try:     
            rr = requests.request("GET",headers=headers2,url=url)
            io=json.loads(rr.text)
                #print(io)
            aed = io["resultado"]["accesoSimetrico"]
            haed = io["resultado"]["codigoAutentificacionHash"]
         
            
            idOrdenPago2=descifrar_aes_gcm(idOrdenPago, aed, haed)
            idOrdenPago23=cifrar_datosRSA(idOrdenPago2,'')
            event3.update({"idOrdenPago":idOrdenPago23})
        except Exception as e:
            print(f"Error al obtener la información de acceso: {str(e)}")

        # Calcula la diferencia de tiempo
        end_time = datetime.now()
        time_elapsed = end_time - start_time
           # tos=time_elapsed.total_seconds()
        start_time=start_time.strftime("%Y-%m-%d %H:%M:%S")
            
        escritura_log('LBD_MCAMBIO-PY',event3,io,str(time_elapsed.total_seconds()),start_time)
        event=event3
    else:
        print(event)
            # Calcula la diferencia de tiempo
        end_time = datetime.now()
        time_elapsed = end_time - start_time
        start_time=start_time.strftime("%Y-%m-%d %H:%M:%S")
        escritura_log('LBD_MCAMBIO-PY',event,event,str(time_elapsed.total_seconds()),start_time)
        
    respuesta = {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': "*",
           'Access-Control-Allow-Headers': "origin, content-type, accept, authorization,x-request-id,x-id-acceso",
            'Access-Control-Allow-Methods': "GET, POST, PUT, DELETE, OPTIONS, HEAD",
            'Access-Control-Allow-Credentials': True},
        'body':json.dumps(event)
        
            }
    
    return respuesta




def obj_dict(obj):
    return obj.__dict__