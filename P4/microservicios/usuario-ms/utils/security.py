import hashlib

def encriptar(password):
    return hashlib.sha256(password.encode()).hexdigest()
