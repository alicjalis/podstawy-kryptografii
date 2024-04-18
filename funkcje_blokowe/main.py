from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import time

def encrypt_data(data, key, mode):
    cipher = AES.new(key, mode)
    ciphertext = cipher.encrypt(data)
    return ciphertext

def decrypt_data(ciphertext, key, mode):
    cipher = AES.new(key, mode)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def measure_time(data_size, key, mode, num_measurements=50):
    data = get_random_bytes(data_size)

    total_encrypt_time = 0
    total_decrypt_time = 0

    for _ in range(num_measurements):
        start_encrypt = time.time()
        ciphertext = encrypt_data(data, key, mode)
        end_encrypt = time.time()
        total_encrypt_time += end_encrypt - start_encrypt

        start_decrypt = time.time()
        decrypted_data = decrypt_data(ciphertext, key, mode)
        end_decrypt = time.time()
        total_decrypt_time += end_decrypt - start_decrypt

    avg_encrypt_time = total_encrypt_time / num_measurements
    avg_decrypt_time = total_decrypt_time / num_measurements

    return avg_encrypt_time, avg_decrypt_time


data_sizes = [1024 * 1024, 1024 * 1024 * 3, 1024 * 1024 * 10]  # 1MB, 3MB, 10MB

key = get_random_bytes(16)

modes = [AES.MODE_ECB, AES.MODE_CBC, AES.MODE_OFB, AES.MODE_CFB, AES.MODE_CTR]
mode_names = ['ECB', 'CBC', 'OFB', 'CFB', 'CTR']

for data_size in data_sizes:
    print(f"Data Size: {data_size / (1024 * 1024)} MB")
    for mode, mode_name in zip(modes, mode_names):
        avg_encrypt_time, avg_decrypt_time = measure_time(data_size, key, mode)
        print(
            f"Mode: {mode_name}, Average Encryption Time: {avg_encrypt_time:.6f} s, Average Decryption Time: {avg_decrypt_time:.6f} s")
    print()
