import random
import datetime

import jwt
from jwt import exceptions

from itegrateSys import settings

JWT_SALT = settings.SECRET_KEY

SECRET_KEY_16 = JWT_SALT[:16]
class TokenAuth:

    @staticmethod
    def create_token(payload, timeout=60 * 12):
        """
        :param payload:  例如：{'user_id':1,'username':'wupeiqi'}用户信息
        :param timeout: token的过期时间，默认20分钟
        :return:
        """
        headers = {'typ': 'jwt', 'alg': 'HS256'}
        payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=timeout)
        result = jwt.encode(payload=payload, key=JWT_SALT, algorithm="HS256", headers=headers).decode('utf-8')
        return result

    @staticmethod
    def parse_payload(token):
        """
        对token进行和发行校验并获取payload
        :param token:
        :return:
        """
        result = {'status': False, 'data': None, 'error': None}
        try:
            verified_payload = jwt.decode(token, JWT_SALT, True)
            result['status'] = True
            result['data'] = verified_payload
        except exceptions.ExpiredSignatureError:
            result['error'] = 'token已失效'
        except jwt.DecodeError:
            result['error'] = 'token认证失败'
        except jwt.InvalidTokenError:
            result['error'] = '非法的token'
        return result


from Cryptodome.Cipher import AES
from Cryptodome import Random
from binascii import b2a_hex


def encryption_password(password):
    # 要加密的明文
    data = password
    # 密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.
    # 目前AES-128足够用
    key = SECRET_KEY_16.encode('utf8')
    # 生成长度等于AES块大小的不可重复的密钥向量
    iv = Random.new().read(AES.block_size)

    # 使用key和iv初始化AES对象, 使用MODE_CFB模式
    mycipher = AES.new(key, AES.MODE_CFB, iv)
    # 加密的明文长度必须为16的倍数，如果长度不为16的倍数，则需要补足为16的倍数
    # 将iv（密钥向量）加到加密的密文开头，一起传输
    ciphertext = iv + mycipher.encrypt(data.encode())

    # 解密的话要用key和iv生成新的AES对象
    mydecrypt = AES.new(key, AES.MODE_CFB, ciphertext[:16])
    # 使用新生成的AES对象，将加密的密文解密
    decrypttext = mydecrypt.decrypt(ciphertext[16:])

    # print('密钥k为：', key)
    # print('iv为：', b2a_hex(ciphertext)[:16])
    # print('加密后数据为：', b2a_hex(ciphertext)[16:])
    # print('解密后数据为：', decrypttext.decode())
    return b2a_hex(ciphertext)[16:]


def decryption_password(password):
    # 要加密的明文
    data = password
    # 密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.
    # 目前AES-128足够用
    key = SECRET_KEY_16.encode('utf8')
    # 生成长度等于AES块大小的不可重复的密钥向量
    iv = Random.new().read(AES.block_size)

    # 使用key和iv初始化AES对象, 使用MODE_CFB模式
    mycipher = AES.new(key, AES.MODE_CFB, iv)
    # 加密的明文长度必须为16的倍数，如果长度不为16的倍数，则需要补足为16的倍数
    # 将iv（密钥向量）加到加密的密文开头，一起传输
    ciphertext = iv + mycipher.encrypt(data.encode())

    # 解密的话要用key和iv生成新的AES对象
    mydecrypt = AES.new(key, AES.MODE_CFB, ciphertext[:16])
    # 使用新生成的AES对象，将加密的密文解密
    decrypttext = mydecrypt.decrypt(ciphertext[16:])
    return decrypttext.decode('utf8')

