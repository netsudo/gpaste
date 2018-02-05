import os
import base64
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend

class Encrypt:
    def __fernetKey(self, salt, password):
        backend = default_backend()

        kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1, backend=backend)
        key = base64.urlsafe_b64encode(kdf.derive(b"%a" % password))

        return Fernet(key)

    def encryptContent(self, content, password):
        salt = os.urandom(16)
        f = self.__fernetKey(salt, password)
        token = f.encrypt(b"%a" % content)

        return salt, token

    def unencryptContent(self, salt, token, password):
        f = self.__fernetKey(salt, password)

        try:
            return f.decrypt(token)
        except InvalidToken:
            return False
