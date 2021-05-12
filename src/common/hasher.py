import bcrypt
import base64

from Cryptodome.Cipher import AES
from Cryptodome import Random
from Cryptodome.Protocol.KDF import PBKDF2
from django.conf import settings

BLOCK_SIZE = 16

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) * BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


def get_private_key(random):
    salt = settings.SECRET_KEY
    kdf = PBKDF2(random, salt, 64, 1000)
    key = kdf[:32]
    return key


def encrypt(raw, random):
    private_key = get_private_key(random)
    raw = pad(raw).encode('utf-8')
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))


def decrypt(enc, random):
    private_key = get_private_key(random)

    # base64로 decode
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))


# 비밀번호를 암호화합니다.
def hash_str(_str):
    hashed_str = bcrypt.hashpw(_str.encode('utf-8'), bcrypt.gensalt())
    return hashed_str.decode('utf-8')  # db에 저장하기 위해서 문자열로 변환


# 비밀번호를 확인합니다.
def check_str(input_str, stored_str):
    bytes_input_str = input_str.encode('utf-8')
    bytes_stored_str = stored_str.encode('utf-8')
    return bcrypt.checkpw(bytes_input_str, bytes_stored_str)
