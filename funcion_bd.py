import json
import os
import datetime
import time
#import psycopg2
#from psycopg2 import Error

class ConectaBD:

    def __init__(self):
        #Entorno de horario local
        os.environ['TZ'] = 'America/Mexico_City'
        time.tzset()
        
        #Conexión mediante variables de entorno 
        try:
            print("Conectando con host PG.... [Base de Datos]")
            self.connection =  psycopg2.connect(user=os.environ['usuario'],
                                  password= os.environ['contrasena'],
                                  host= os.environ['endpoint'],
                                  port="1522",
                                  database= os.environ['nombre_base_datos']
                                  )
            #Instancia del cursor
            self.cursor = self.connection.cursor()
            print("Base de datos conectada exitosamente [Base de Datos]")
            print(self.cursor)
        except Exception as err:
            print("Error Base de datos no puede conectar [Base de Datos]")
            raise err
    
    def obtener_datos(self, data):
        return self.__obtener_datos_info(data)
        
    def __obtener_datos_info(self, data):
        print("Información Base de datos PostgreSQL [Base de Datos]")
        print("PostgreSQL server information")
        response = {}
        response['body'] = {}
        #query_id = "SELECT SC_CATREM.FNCATELEMENTOS('c',"+data+"); FETCH ALL IN "'c'" "
        query_id = "select * from sc_usuarios.fnestatus_r(null)"
        print (query_id)
        
        try:
            self.cursor.execute(query_id)
            print("Elementos: ", self.cursor.rowcount)
            response_id = self.cursor.fetchall()
            len_resultset = len(response_id)
            print (len_resultset)
            row = self.cursor.fetchone()
            while row is not None:
                print(":P"+row)
                row = self.cursor.fetchone()
        
        except Exception as err:
            raise err 
            
        self.cursor.close()
        self.connection.close()    
        print (response_id)
        return (response_id)
            
    