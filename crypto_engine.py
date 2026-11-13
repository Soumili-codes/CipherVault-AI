
import os
import json
import base64

from argon2.low_level import hash_secret_raw, Type
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def derive_key(password, salt):
    """Generate a secure encryption key from a password."""

    return hash_secret_raw(
        secret=password.encode("utf-8"),
        salt=salt,
        time_cost=3,
        memory_cost=65536,
        parallelism=2,
        hash_len=32,
        type=Type.ID
    )


def encrypt_data(file_data, password):
    """Encrypt file data using AES-256-GCM."""

    salt = os.urandom(16)
    nonce = os.urandom(12)

    key = derive_key(password, salt)

    aes = AESGCM(key)
    encrypted_data = aes.encrypt(nonce, file_data, None)

    result = {
        "version": 1,
        "salt": base64.b64encode(salt).decode(),
        "nonce": base64.b64encode(nonce).decode(),
        "data": base64.b64encode(encrypted_data).decode()
    }

    return json.dumps(result).encode("utf-8")


def decrypt_data(encrypted_file, password):
    """Decrypt data and verify its authenticity."""

    result = json.loads(encrypted_file.decode("utf-8"))

    salt = base64.b64decode(result["salt"], validate=True)
    nonce = base64.b64decode(result["nonce"], validate=True)
    encrypted_data = base64.b64decode(result["data"], validate=True)

    if result["version"] != 1:
        raise ValueError("Unsupported file format")

    if len(salt) != 16 or len(nonce) != 12:
        raise ValueError("Invalid encrypted file format")

    key = derive_key(password, salt)

    aes = AESGCM(key)

    return aes.decrypt(nonce, encrypted_data, None)
