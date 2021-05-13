import hashlib
import bcrypt
import base64

from Cryptodome.Cipher import AES
from Cryptodome import Random
from django.conf import settings


class AESCipher:
    BLOCK_SIZE = 16
    key = hashlib.sha256(settings.SECRET_KEY.encode('utf-8')).digest()

    def pad(self, s):
        return s + (self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE) * chr(self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE)

    def unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]

    def encrypt(self, raw):
        raw = self.pad(raw).encode('utf-8')
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self.unpad(cipher.decrypt(enc[16:]))

    def encrypt_str(self, raw):
        return self.encrypt(raw).decode('utf-8')

    def decrypt_str(self, enc):
        if type(enc) == str:
            enc = str.encode(enc)
        return self.decrypt(enc).decode('utf-8')


# 비밀번호를 암호화합니다.
def hash_str(_str):
    hashed_str = bcrypt.hashpw(_str.encode('utf-8'), bcrypt.gensalt())
    return hashed_str.decode('utf-8')  # db에 저장하기 위해서 문자열로 변환


# 비밀번호를 확인합니다.
def check_str(input_str, stored_str):
    bytes_input_str = input_str.encode('utf-8')
    bytes_stored_str = stored_str.encode('utf-8')
    return bcrypt.checkpw(bytes_input_str, bytes_stored_str)
