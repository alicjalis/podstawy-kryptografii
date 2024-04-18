from random import getrandbits
from Crypto.Cipher import AES


def padding(x):
    padding_length = AES.block_size - len(x) % AES.block_size
    return x + b'\0' * padding_length

def strip(x):
    return x.rstrip(b'\0')

def hex_rep(x):
    hex_list = []
    for b in x:
        hex_list.append(f'{b:02X}')
    return ' '.join(hex_list)

def cipher_params(cipher, mode):
    if mode in [AES.MODE_CBC, AES.MODE_OFB, AES.MODE_CFB]: return dict(iv=cipher.iv)
    if mode in [AES.MODE_CTR]: return dict(nonce=cipher.nonce)
    return {}
modenames = 'ECB CBC OFB CTR CFB'.split()
modes = [AES.MODE_ECB, AES.MODE_CBC, AES.MODE_OFB, AES.MODE_CTR, AES.MODE_CFB]
key = getrandbits(16*8).to_bytes(16, byteorder='little')

with open('test_prop.txt', 'rb') as f:
    test = f.read()

print('oryginalny tekst:')
print(test,"\n")

for mode, name in zip(modes, modenames):
    c1 = AES.new(key, mode)
    encrypted = c1.encrypt(padding(test))

    encrypted = bytearray(encrypted)
    encrypted[1] = 2

    c2 = AES.new(key, mode, **cipher_params(c1, mode))
    decrypted = strip(c2.decrypt(encrypted))
    print(name)
    print(decrypted)
    print()