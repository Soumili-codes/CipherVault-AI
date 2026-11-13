
from pathlib import Path
from crypto_engine import encrypt_data, decrypt_data


def encrypt_file(input_path, password, output_path):
    input_file = Path(input_path)
    output_file = Path(output_path)

    # Read original file
    file_data = input_file.read_bytes()

    # Encrypt file data
    encrypted_data = encrypt_data(file_data, password)

    # Save encrypted file
    output_file.write_bytes(encrypted_data)

    print("File encrypted successfully!")


def decrypt_file(input_path, password, output_path):
    input_file = Path(input_path)
    output_file = Path(output_path)

    # Read encrypted file
    encrypted_data = input_file.read_bytes()

    # Decrypt file data
    decrypted_data = decrypt_data(encrypted_data, password)

    # Save decrypted file
    output_file.write_bytes(decrypted_data)

    print("File decrypted successfully!")
