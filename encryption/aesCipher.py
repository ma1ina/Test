from Crypto.Cipher import AES
import base64


def encode(data,key):
    iv = b"0123456789abcdef"
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(data)
    
def decode(data,key):
    iv=b"0123456789abcdef"
    cipher=AES.new(key, AES.MODE_CBC, iv)
    return cipher.decrypt(data)