import hashlib
import os

def encriptar(password):
    '''GENERAMOS UN HASH 256 CON SALTING  PARA MAS PLACER :D'''
    
    salt = os.urandom(16) # bytes
    password_bytes = password.encode('utf-8') 
    
    hashed_password = hashlib.sha256(salt + password_bytes).hexdigest()
    salt_hex = salt.hex()
    
    return f"{salt_hex}${hashed_password}"

def verificar_password(password, hashed_password):
    '''VERIFICAMOS SI EL PASSWORD ES EL CORRECTO'''
    
    salt_hex, hashed = hashed_password.split('$')
    salt = bytes.fromhex(salt_hex)
    
    password_bytes = password.encode('utf-8')
    
    return hashed == hashlib.sha256(salt + password_bytes).hexdigest() #! RETORNA TRUE O FALSE



