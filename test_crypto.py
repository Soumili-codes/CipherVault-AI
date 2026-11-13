
from crypto_engine import encrypt_data, decrypt_data

message = b"Hello! This is my first encrypted file."

password = "TestPassword123!"

# Encrypt
encrypted = encrypt_data(message, password)

print("Encryption successful!")

# Decrypt
decrypted = decrypt_data(encrypted, password)

print("Decryption successful!")
print("Original message:", decrypted.decode())

# Verify
assert decrypted == message

print("TEST PASSED!")
# Test wrong password
try:
    decrypt_data(encrypted, "WrongPassword123!")
    print("ERROR: Wrong password was accepted!")

except Exception:
    print("Wrong password rejected successfully!")

# Test file tampering
import json
import base64

tampered = json.loads(encrypted.decode("utf-8"))

# Change one byte of encrypted data
ciphertext = bytearray(
    base64.b64decode(tampered["data"])
)

ciphertext[0] ^= 1

tampered["data"] = base64.b64encode(
    ciphertext
).decode("utf-8")

tampered_file = json.dumps(tampered).encode("utf-8")

try:
    decrypt_data(tampered_file, password)
    print("ERROR: Tampered data was accepted!")

except Exception:
    print("Tampering detected successfully!")
