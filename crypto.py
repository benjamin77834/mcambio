from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import ast
from Crypto.PublicKey import RSA
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
#from Crypto.Cipher import AES, PKCS1_OAEP

from Crypto.Cipher import PKCS1_OAEP
#from cryptography.hazmat.primitives.asymmetric import rsa, padding

import os
import base64

from base64 import b64decode
from base64 import b64encode
import datetime as datetime
from datetime import datetime
import time

def es_diccionario(cadena):
    try:
        # Intenta evaluar la cadena como un diccionario
        diccionario = ast.literal_eval(cadena)
        if isinstance(diccionario, dict):
            return True
        else:
            return False
    except (SyntaxError, ValueError):
        # Si hay un error al evaluar la cadena, no es un diccionario válido
        return False

def cifrar_aes_gcm(dato, acceso_simetrico, codigo_autentificacion_hash):
    try:
        acceso_simetrico=b64decode(acceso_simetrico)
        decoded_key = base64.b64decode(acceso_simetrico.encode('utf-8'))
       # decoded_key = base64.b64decode(acceso_simetrico)
        #secret_key = decoded_key
        #associated_data = codigo_autentificacion_hash.encode('utf-8')
        #iv = os.urandom(12)
        #cipher = Cipher(algorithms.AES(secret_key), modes.GCM(iv), backend=default_backend())
        #encryptor = cipher.encryptor()
        #encryptor.authenticate_additional_data(associated_data)
        #ciphertext = encryptor.update(dato.encode('utf-8')) + encryptor.finalize()
       # tag = encryptor.tag
      #  encrypted_data = iv + ciphertext + tag
     #   encrypted_base64 = base64.b64encode(encrypted_data).decode('utf-8')
        encrypted_base64=''
    except Exception:
        return "", False
    return encrypted_base64, True
    
    
def descifrar_aes_gcm(dato, acceso_simetrico, codigo_autentificacion_hash):
    try:
        decoded_key = base64.b64decode(acceso_simetrico)
        secret_key = decoded_key
        associated_data = codigo_autentificacion_hash.encode('utf-8')
        encrypted_data = base64.b64decode(dato)
        iv = encrypted_data[:12]
        ciphertext = encrypted_data[12:-16]
        tag = encrypted_data[-16:]
        cipher = Cipher(algorithms.AES(secret_key), modes.GCM(iv, tag), backend=default_backend())
        decryptor = cipher.decryptor()
        decryptor.authenticate_additional_data(associated_data)
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    except Exception:
        return "", False
    return plaintext.decode('utf-8')
    
    
def decifrarRequest(acceso_simetrico,codigo_autentificacion_hash, text):
    error = True
    for k, v in text.items():
        if isinstance(v, dict):
            text[k], error = decifrarRequest(acceso_simetrico,codigo_autentificacion_hash, v)
        elif k != "identificador":
            if isinstance(v, str) and k.startswith("*"):
                v, error = descifrar_aes_gcm(v,acceso_simetrico, codigo_autentificacion_hash)
                if error:
                    text[k] = v
                else:
                    break
            elif isinstance(v, list):
                for i in range(len(v)):
                    v[i], error = decifrarRequest(acceso_simetrico,codigo_autentificacion_hash, v[i])
                    if not error:
                        break
    return text, error
    
def cifrarResponse(acceso_simetrico,codigo_autentificacion_hash, text):
    error = True
    for k, v in text.items():
        if isinstance(v, dict):
            text[k], error = cifrarResponse(acceso_simetrico,codigo_autentificacion_hash, v)
        elif k != "identificador":
            if isinstance(v, str) and k.startswith("*"):
                v, error = cifrar_aes_gcm(v,acceso_simetrico,codigo_autentificacion_hash)
                if error:
                    text[k] = v
                else:
                    break
            elif isinstance(v, list):
                for i in range(len(v)):
                    v[i], error = cifrarResponse(acceso_simetrico,codigo_autentificacion_hash, v[i])
                    if not error:
                        break
    return text, error
    
    
def descifrar_datosRSA(datos_cifrados, clave_privada):
#    print("--------datos_cifrados_para_descrifrar--------:")
   # print(datos_cifrados)
    #print(clave_privada)
    encrypted_message = b64decode(datos_cifrados.encode())
    rt = os.environ["key_rsa_private"]
    key = RSA.importKey(b64decode(clave_privada))
    cipher = PKCS1_OAEP.new(key)
    message = cipher.decrypt(encrypted_message).decode()
    #print(message)
    return message
   
def  descifrar_datosRSA2(datos_cifrados,clave_privada):  
    encrypted_message = b64decode(datos_cifrados.encode())

    key = RSA.importKey(b64decode(clave_privada))
    cipher = PKCS1_OAEP.new(key, hashAlgo=SHA256)
    message = cipher.decrypt(encrypted_message).decode()
    print
    return message
    #return message.decode('utf-8')
    

def cifrar_datosRSA2(datos_cifrados,clave_pub):      
    key = RSA.importKey(b64decode(clave_pub))
    cipher = PKCS1_OAEP.new(key,hashAlgo=SHA256)
    message_encrypted = cipher.encrypt(datos_cifrados.encode())
    encode = b64encode(message_encrypted).decode("UTF-8")
    return encode

    
    
    
def cifrar_datosRSA(datos_cifrados, clave_privada):
    #print(datos_cifrados)
    #print(clave_privada)
    #message="Mensaje de prueba"
 
    rt = os.environ["key_rsa_public"]
    key = RSA.importKey(b64decode(rt))
    cipher = PKCS1_OAEP.new(key)
    message_encrypted = cipher.encrypt(datos_cifrados.encode())

    encode = b64encode(message_encrypted).decode("UTF-8")
#encode


    #print(message_encrypted)
    return(encode)

def escritura_log(self,request,response,tiempo_total,start):
   # now = time.ctime()
    #request = request.replace('\n','')
    #response = response.replace('\n','')
    #request = request.replace('','\\')
    #response = response.replace('','\\')
    log_data = {"log_data":{"fecha": start,
            "Level": "INFO",
            "Mensaje": {"Peticion": request, "Respuesta": response},
            "Servicios": ["Arquetipo "],
            "TiempoTotal": tiempo_total }}
    print(log_data)
    
def escritura_log2(servio,request,response,start_time):
    
    end_time = datetime.now()
    tiempo_total = end_time - start_time
    tiempo_total = tiempo_total.total_seconds()
    #if es_diccionario(request)=='False':
    #    request=json.loads(request)
    #if es_diccionario(response)=='False':
    #    response=json.loads(response)
    #    response = response.replace('"', "'")
    #    print(response)
        
    fe=end_time.strftime("%Y-%m-%d %H:%M:%S")
    log_data = {'log_data':{'fecha':fe,
            'Level': 'INFO',
            'Mensaje': {'Peticion': request, 'Respuesta':response},
            'Servicios': [servio],
            'TiempoTotal': tiempo_total }}
    print(log_data)    
    
    
def encryptaes(plaintext, key):
    aesgcm = AESGCM(key)
    nonce = AESGCM.generate_nonce()
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)
    return ciphertext

def decryptaes(nonce, ciphertext, key):
    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)
    return plaintext
    
    
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from base64 import urlsafe_b64encode, urlsafe_b64decode    
    
def aes_gcm_decrypt(encrypted_data_base64, secret_key, haed):
    encrypted_data = base64.b64decode(encrypted_data_base64)
    decoded_key = base64.b64decode(secret_key)
    associated_data = haed.encode('utf-8')

    iv = encrypted_data[:12]
    ciphertext = encrypted_data[12:-16]
    tag = encrypted_data[-16:]

    cipher = Cipher(algorithms.AES(decoded_key), modes.GCM(iv, tag), backend=default_backend())
    decryptor = cipher.decryptor()

    decryptor.authenticate_additional_data(associated_data)
    decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()

    return decrypted_message.decode('utf-8')
    
def aes_ec(dato,aed,haed):
    decoded_key = base64.b64decode(aed)
    secret_key = decoded_key
    associated_data = haed.encode('utf-8')
    iv = os.urandom(12)
    cipher = Cipher(algorithms.AES(secret_key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encryptor.authenticate_additional_data(associated_data)
    ciphertext = encryptor.update(dato.encode('utf-8')) + encryptor.finalize()
    tag = encryptor.tag
    encrypted_data = iv + ciphertext + tag
    encrypted_base64 = base64.b64encode(encrypted_data).decode('utf-8')

    return(encrypted_base64)
    
    
def cifrar_datosRSA3(datos_cifrados,key_priv):
    message=datos_cifrados.encode('utf-8')
    key = RSA.importKey(b64decode(key_priv))

    cipher = PKCS1_OAEP.new(key, hashAlgo=SHA256)
    #print(str(message))
    cipher_text = cipher.encrypt(message)
        #print("Original Message:", message)
        #print("Encrypted Message:", cipher_text)

    encrypted_message_str = base64.b64encode(cipher_text).decode('utf-8')
        #print(encrypted_message_str)

    return encrypted_message_str
    
    
def cif_rsa(message,key_pub):
    print("message:")
    print(message)
    message=message.encode('utf-8')
    message=base64.b64encode(message)

#       message=b64decode(message)
    print("messageb64:")
    print(message)
    key = RSA.importKey(b64decode(key_pub))
#       print(key)
    cipher = PKCS1_OAEP.new(key)
        #message=message.encode('utf-8')
    cipher_text1 = cipher.encrypt(message)
#       print("cifrado>>>")
#       print(cipher_text1)
    encode=b64encode(cipher_text1).decode("UTF-8")
#       print("cifrado>>>")
#       print(encode)
        #return encode
    return encode

def des_rsa(cipher_text1,key_pub):
    message=base64.b64decode(cipher_text1)
    key = RSA.importKey(b64decode(key_priv))
    cipher = PKCS1_OAEP.new(key)
    cipher_text = cipher.decrypt(message)
    encode=b64encode(cipher_text).decode("UTF-8")
    return encode        
     
    
def actualizar_valor2(lista,identificador,clave_pub,aed,haed):
    print("arreglo:")
    for diccionario in lista:
      #  print(diccionario["valor"])
        pva=diccionario["valor"]
        print(pva)
        pva=aes_gcm_decrypt(pva,aed,haed)
        print("aesdec:")
        print(pva)
        cahc=cifrar_datosRSA2(pva,clave_pub)                 
        diccionario["valor"] =cahc
        print("rsa:")
        print(cahc)
         #break  # Termina la iteración después de actualizar el valor
    return lista
    
    
def verifica_valor2(lista):
    for diccionario in lista:
        print(diccionario["valor"])
        if len(str(diccionario["valor"]))>0:
            yu="ok"
           # print(yu)
        else: 
            yu="no-ok"
            #print(yu)
            return yu
    return yu    