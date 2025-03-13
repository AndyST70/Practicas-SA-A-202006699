import hashlib
import os

def encriptar(password):
    salt = os.urandom(16)
    password_bytes = password.encode('utf-8')
    hashed_password = hashlib.sha256(salt + password_bytes).hexdigest()
    return f"{salt.hex()}${hashed_password}"

def verificar_password(password, hashed_password):
    salt_hex, hashed = hashed_password.split('$')
    salt = bytes.fromhex(salt_hex)
    return hashed == hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
