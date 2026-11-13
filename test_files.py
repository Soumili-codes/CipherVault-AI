
from file_manager import encrypt_file, decrypt_file

password = "TestPassword123!"

# Encrypt sample file
encrypt_file(
    "samples/secret.txt",
    password,
    "samples/secret.enc"
)

# Decrypt encrypted file
decrypt_file(
    "samples/secret.enc",
    password,
    "samples/recovered.txt"
)

# Compare original and recovered files
with open("samples/secret.txt", "rb") as original:
    original_data = original.read()

with open("samples/recovered.txt", "rb") as recovered:
    recovered_data = recovered.read()

assert original_data == recovered_data

print("FILE ENCRYPTION TEST PASSED!")
