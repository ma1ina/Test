import base64
from Crypto.Cipher import AES
import hashlib

def _encode(data,key,iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(data)

def _div_to_16_bytes(line):
    line = base64.b64encode(bytearray(line, encoding="utf-8"))
    chunks, chunk_size = len(line), 16
    tab = [line[i:i + chunk_size] for i in range(0, chunks, chunk_size)]
    tab[-1] = bytearray(tab[-1])
    while len(tab[-1]) != 16:
        tab[-1].append(61)
    return tab

def getCipher(inputText, key,iv):
    key = hashlib.sha3_256(bytes(key, encoding="utf-8")).digest()
    TabLines = _div_to_16_bytes(inputText)
    EncryptedInputTextList = list(map(_encode, TabLines, [key] * len(TabLines),[iv]*len(TabLines)))
    return EncryptedInputTextList