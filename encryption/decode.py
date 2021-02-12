import base64
from Crypto.Cipher import AES
import hashlib


def _decode(data,key,iv):
    cipher=AES.new(key, AES.MODE_CBC, iv)
    return cipher.decrypt(data)
def _div_to_16_bytes(EncryptedLine):
    chunks, chunk_size = len(EncryptedLine), 16
    Tab = [EncryptedLine[i:i + chunk_size] for i in range(0, chunks, chunk_size)]
    return Tab
def getPlainText(encrypedText,key,iv):
    Encrypted16BytesTable=_div_to_16_bytes(encrypedText)
    PlainTextList = list(map(_decode, Encrypted16BytesTable, [key] * len(Encrypted16BytesTable), [iv]*len(Encrypted16BytesTable)))
    return PlainTextList