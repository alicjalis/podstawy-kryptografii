from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import time

def generate_random_bytes(size):
    return os.urandom(size)

def encrypt_decrypt(mode, plaintext, key):
    backend = default_backend()
    iv = os.urandom(16)  # Initialization vector for CBC mode

    if mode == 'ECB':
        cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    elif mode == 'CBC':
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    elif mode == 'OFB':
        cipher = Cipher(algorithms.AES(key), modes.OFB(iv), backend=backend)
    elif mode == 'CFB':
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
    elif mode == 'CTR':
        cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=backend)
    else:
        raise ValueError("Invalid mode")

    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()

    return ciphertext, decrypted_text

def measure_time(mode, data_size):
    key = os.urandom(32)  # 256-bit key
    plaintext = generate_random_bytes(data_size)

    start_time = time.time()
    ciphertext, decrypted_text = encrypt_decrypt(mode, plaintext, key)
    end_time = time.time()

    return end_time - start_time

modes = ['ECB', 'CBC', 'OFB', 'CFB', 'CTR']
data_sizes = [1000, 10000, 100000]  # Mały, średni, duży rozmiar pliku

for mode in modes:
    print(f"Mode: {mode}")
    for size in data_sizes:
        encryption_time = measure_time(mode, size)
        print(f"Data size: {size} bytes, Encryption time: {encryption_time} seconds")
