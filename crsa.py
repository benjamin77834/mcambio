import sys
import base64
#from Crypto.PublicKey import RSA
#from Crypto.Cipher import PKCS1_OAEP


#from Cryptodome.Cipher import PKCS1_v1_5
#from Cryptodome.PublicKey import RSA
#from Cryptodome.Random import get_random_bytes

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Random import get_random_bytes


def crsa(bit_size,key_format,text2cipher,cifrado):
    
    private_key_pem = '''-----BEGIN RSA PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCVD0/KQ1Otr20IpdYHyOTj/Bex4kNCHbSRNqX15SNQmAa05wU6Gf96a7zR8TLQgU5oeNNlUJqkxI1m0GzGWDT96KM7U0r7BIxvy4x6rFISnXWqDHKwQV53JRxONvnIwSbNAJ1+oRbJ4L075ai4kVd8RApfeePnv4KPY6IQaNBtMW4c1PzZgD8s/7vmF4KHTJ47ROr3ugPRguFqVH9bXjG+pf6JxRmvgMgRDOnxYgCO/1mqT6tm2LztBdy24t8AjxqTClVeMLi4UD6T1Ep9zztULubsPTQWUsaM5IK2Vv/TDxaxIxLzNw9PPh4oQs5yo9C+RfWMW3vveyi6z2rwlP+pAgMBAAECggEBAJRILhzMyzJt3+6JYphN7f0qa7vmlPfxqw4GKiSqdG4ZPhq58sYw1KhJAwZqhh1LdN+SyuDvxVcBvJS55GuPle+8fJ1op598j+Qqvi3OvLqN715hkbnq3Xly7myUXfmqw9mNsh8lSxE6w6UROr2YwEn7OcJu9Bw3tD7GY5MlYaosyxh9HKagQNEv3/9Aic+20e8SqjdT3K3ykjrltPPKP0OOfnq//9emv+GE8Ec+t+CMemvNEyiWamVCcrO44iT93Kfer9JGwmdts6cTQCrCijeoRg3Adnd6pzz5xSEt+Dw0tFx7RwZGBSrnQ+Bp+AtuifaXzWjk/4Sa5ag5+26JFQECgYEA1EfHxZ3JfUa7td7gTonMmzzBFLjM2HH9P/GEQZt1kdyy4ATioU4/4G5BfmfM2sSVWjbk7V14P6jekpge8AdoNa1RsigLQgu8ZJsVqQiaw3jSKmOipXAQn5s3nBDxnFczuBnZBVM0ygWJ75GZ+lJTopQo4/sRvO1cUIbL+9xQJuECgYEAs8JOCW/5d1B5znwaXYOO8z6kqK08Bmd39xdkiW859Cloi+ZWzb9QmwR3tDo5cYQD3nErQIGA7X33dHD32EEDnEA42Evk2e2ZWzkifz2dtxJehDGIDsoApPfqNDK/kzM9tAHhZbbLk/6evD2qcNCgc7GYxVcNxLQagipI1d2qmckCgYAy3eBo4h5d/o0MT5PAPhThPfWmWYH8e5QLtnvSnMXXZeMW+xSzQmTcCo93Erhr059WNsE0f6lI19Y9mmYPbjbyZc2luyK3eMhz8xWFo6IyJMl3jthyfB//ntn8c7Lxm5OxEcCHHiEQJ7OdzG3xJbkUxBvoRUlC1D3CrgpDF8+9AQKBgQCP4pXoQ/LhKE93kirgc2+3EItoYNHNJoEGDXlx8M/oukRuxv7wTZTNoHPYlUpprIwUP22pgn+amdu7HrmkJdYn+dgGeilCr0azmDYet0lIwrFZCvSnMdX2NmMHSR/DSZ64OVEbw4eMfKC+eHW3O6dTM/Le8uGYc7lMO2B1n6rw0QKBgHV2LWW5uJFAY2JTZIAWoAWOdvRtFjNPGAvT4Wjf9hgtN9/K+8ODlYdHmJ6g1LQcqGNm/WdS++4DcaaR1lBjDlq9LjUErY+Wume1LYigq+l+4a5WBGcozMtojfGHCAy84cN87e4VlY4ANqVZx1q3v8GbBcGdcMCBlSFd9pcK+203
-----END RSA PRIVATE KEY-----'''

    s = "DAjlEwf6NcRQ3apsP5ieWMHl38Xs+yMtlxTl9tGEJ2Vnv3BNauTgWao0iDRu6RKImCM2pDsCUL1sVkunRG1vox8x1KxsbVB5MEkFCekAS4jU5X2Vm1madtUsMQIksYvKEEZAaDlZAMx3fdnBYfLRzdyPPQke8m2zwopL4QjT2ukvQAOLhH5J4oov1cnMoy/CW47ly37DlQDE2EpKqsxHIYIpsEtvXHlnb3mpZ8gbHkkPl+7SZQ5bbE2K4rqv0nzpAL/t0DVkeRJItc3Q8W6/ZYLY2eQjBctfB+F+ijifF3pECVr8rbixUUc5Hb3jLK8M60GZglU4LLYq6s6aUy5MaQ=="

    code_bytes = s.encode('UTF-8')
    by = base64.b64decode(code_bytes)
    private_key = RSA.import_key(private_key_pem)
    cipher = PKCS1_v1_5.new(private_key)
    sentinel = get_random_bytes(16)
    rsadecrypt = cipher.decrypt(by[3: 3 + 256], sentinel)
    if rsadecrypt == sentinel:
        print('failure')
    else:
        print(f'success: {rsadecrypt.hex(" ")}')
   
  #  keys = RSA.generate(bit_size)
    
    # Importamos la clave pública para cifrar los datos
   # if cifrado:
    #    cipher_rsa = PKCS1_OAEP.new(keys.publickey())
        # Ciframos los datos.
        #
        # Se deben codificar los datos a 'utf-8', por eso está
        # presente el método '.encode(...)'
     #   enc_data = cipher_rsa.encrypt(text2cipher.encode())
        
      #  print("Encriptado:")
       # print(enc_data, end='nn')
    
        
    #else:    
    # Importamos la clave privada para descifrar los datos
     #   decipher_rsa = PKCS1_OAEP.new(keys)
    
    # Desciframos los datos
      #  enc_data=text2cipher
       # dec_data = decipher_rsa.decrypt(enc_data)
    
    
        print("Desencriptado:")
    #    print(dec_data)