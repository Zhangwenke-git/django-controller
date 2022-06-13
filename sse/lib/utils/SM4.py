from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT
import binascii
from heapq import heappush, heappop
from collections import OrderedDict


class SM4:
    """
    国密sm4加解密
    """

    def __init__(self):
        self.crypt_sm4 = CryptSM4()

    def str_to_hexStr(self, hex_str):
        """
        字符串转hex
        :param hex_str: 字符串
        :return: hex
        """
        hex_data = hex_str.encode('utf-8')
        str_bin = binascii.unhexlify(hex_data)
        return str_bin.decode('utf-8')

    def encrypt(self, encrypt_key, value):
        """
        国密sm4加密
        :param encrypt_key: sm4加密key
        :param value: 待加密的字符串
        :return: sm4加密后的hex值
        """
        crypt_sm4 = self.crypt_sm4
        crypt_sm4.set_key(encrypt_key.encode(), SM4_ENCRYPT)
        encrypt_value = crypt_sm4.crypt_ecb(value.encode())  # bytes类型
        return encrypt_value.hex()

    def decrypt(self, decrypt_key, encrypt_value):
        """
        国密sm4解密
        :param decrypt_key:sm4加密key
        :param encrypt_value: 待解密的hex值
        :return: 原字符串
        """
        crypt_sm4 = self.crypt_sm4
        crypt_sm4.set_key(decrypt_key.encode(), SM4_DECRYPT)
        decrypt_value = crypt_sm4.crypt_ecb(bytes.fromhex(encrypt_value))  # bytes类型
        return self.str_to_hexStr(decrypt_value.hex())


if __name__ == "__main__":

    str_data = """/api/apiproject/;1647615111000;16200245420;eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoieWkubGluMDQiLCJ1c2VybmFtZSI6InlpLmxpbjA0IiwiZXhwIjoxNjQ3NzAwNDg0LCJlbWFpbCI6IjI5OTg2NDUyNUBxcS5jb20ifQ.D-4kYp5nHzaI8C1-Y787Y41b8vKlubqncjKhFGa_tms"""
    key = "20220317.sse.com.cn"
    SM4 = SM4()
    print("待加密内容：", str_data)
    encoding = SM4.encrypt(key, str_data)
    print("国密sm4加密后的结果：", encoding)

    encoding="""f17447923600538aa982ef397ea033
09591a5dddd148c20dbed8bef6b053e288c220aa195cb7e1aee8b709df7c2cc9db601c5e7024555e72c9c657795f8cb06b5477073409a84d2bff45adedb11cac4fef1b011f18cf9d9bc1bdb45cbd64b590d1a757
16d140a61e5c659a1283e995cb15725dadb54fa6a4ddc14a7345c258b87cfc30088885cbe368fc6fb3d4e5f61053c72b8b58d8977aa81c269ceb2a66aba2deccc60d1f586243315a18021c0ac6d70d37ad12803d
c0e48d972e9e1aecf0300b57bd120e406b1adc9da33d2b848cf36dd394c992ae82410186d6cf00901c9f1800b60696e7addd1cc321eb1697f0"""

    print("国密sm4解密后的结果：", SM4.decrypt(key, encoding))
