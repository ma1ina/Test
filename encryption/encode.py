
import hashlib
import splitBytes
import aesCipher


def main():
    line = input("Input text to encode: ")
    key = input("Input password: ")
    return(getCipher(line, key))


def getCipher(line, key):
    key = hashlib.sha3_256(bytes(key, encoding="utf-8"))
    key = key.digest()
    line = splitBytes.div_to_16_bytes(line)
    data = list(map(aesCipher.encode, line, [key] * len(line)))
    return data


if __name__ == "__main__":
    main()
