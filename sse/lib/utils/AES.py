
from Crypto import Random
from Crypto.Cipher import AES
import base64
from hashlib import md5


def pad(data):
    length = 16 - (len(data) % 16)
    return data.encode(encoding='utf-8') + (chr(length) * length).encode(encoding='utf-8')


def unpad(data):
    return data[:-(data[-1] if type(data[-1]) == int else ord(data[-1]))]


def bytes_to_key(data, salt, output=48):
    data = data.encode(encoding='utf-8')
    assert len(salt) == 8, len(salt)
    data += salt
    key = md5(data).digest()
    final_key = key
    while len(final_key) < output:
        key = md5(key + data).digest()
        final_key += key
    return final_key[:output]


def encrypt(message, passphrase):
    salt = Random.new().read(8)
    key_iv = bytes_to_key(passphrase, salt, 32 + 16)
    key = key_iv[:32]
    iv = key_iv[32:]
    aes = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(b"Salted__" + salt + aes.encrypt(pad(message)))


def decrypt(encrypted, passphrase):
    encrypted = base64.b64decode(encrypted)
    assert encrypted[0:8] == b"Salted__"
    salt = encrypted[8:16]
    key_iv = bytes_to_key(passphrase, salt, 32 + 16)
    key = key_iv[:32]
    iv = key_iv[32:]
    aes = AES.new(key, AES.MODE_CBC, iv)
    return unpad(aes.decrypt(encrypted[16:]))


if __name__ == '__main__':
    key = 'seurtl23'
    data = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoieWkubGluMDQiLCJ1c2VybmFtZSI6InlpLmxpbjA0IiwiZXhwIjoxNjQ4MTAyNDEzLCJlbWFpbCI6IjI5OTg2NDUyNUBxcS5jb20ifQ.m4r8wDATai48sP6iWY1EiFafdIztwk0kXfjONEq-tqs'
    encrypt_data = encrypt(data, key)
    print(encrypt_data)

    decrypt_data = decrypt(encrypt_data, key)
    print(decrypt_data)
