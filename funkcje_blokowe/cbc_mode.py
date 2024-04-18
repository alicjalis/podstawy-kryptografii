from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_cbc(data, key, iv):
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_data = b''
    previous_block = iv

    # Podział danych na bloki
    for i in range(0, len(data), AES.block_size):
        block = data[i:i+AES.block_size]

        # Wykonanie operacji XOR z poprzednim blokiem lub IV
        block_xor = bytes([b1 ^ b2 for b1, b2 in zip(block, previous_block)])

        # Szyfrowanie wyniku operacji XOR za pomocą trybu ECB
        encrypted_block = cipher.encrypt(block_xor)

        # Dodanie zaszyfrowanego bloku do zaszyfrowanych danych
        encrypted_data += encrypted_block
        previous_block = encrypted_block  # Ustawienie poprzedniego bloku na bieżący zaszyfrowany blok

    return encrypted_data

def decrypt_cbc(data, key, iv):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = b''
    previous_block = iv

    for i in range(0, len(data), AES.block_size):
        block = data[i:i+AES.block_size]

        # Deszyfrowanie bloku za pomocą trybu ECB
        decrypted_block = cipher.decrypt(block)

        # Wykonanie operacji XOR z poprzednim blokiem lub IV
        decrypted_block_xor = bytes([b1 ^ b2 for b1, b2 in zip(decrypted_block, previous_block)])

        # Dodanie zdeszyfrowanego bloku do zdeszyfrowanych danych
        decrypted_data += decrypted_block_xor
        previous_block = block

    return decrypted_data


plaintext = b'Testowanie dzialania trybu cbc'
key = get_random_bytes(16)
iv = get_random_bytes(AES.block_size)

encrypted_data = encrypt_cbc(pad(plaintext, AES.block_size), key, iv)
decrypted_data = unpad(decrypt_cbc(encrypted_data, key, iv), AES.block_size)

print('--- Original ---')
print(plaintext)
print('--- Encrypted ---')
print(encrypted_data)
print('--- Decrypted ---')
print(decrypted_data)
