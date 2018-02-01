import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend

def encryptContent(content, password):
    backend = default_backend()
    salt = os.urandom(16)

    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1, backend=backend)
    key = base64.urlsafe_b64encode(kdf.derive(b"%a" % password))

    f = Fernet(key)
    token = f.encrypt(b"%a" % content)

    return salt, token

