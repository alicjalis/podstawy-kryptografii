import hashlib

def bit_change_test(input_data):
    original_hash = hashlib.sha256(input_data.encode()).digest()
    changed_hashes = []
    for i in range(len(input_data) * 8):  # dla każdego bitu w wejściu
        modified_input = bytearray(input_data.encode())
        byte_index = i // 8
        bit_index = i % 8
        modified_input[byte_index] ^= (1 << bit_index)  # zmiana pojedynczego bitu
        changed_hash = hashlib.sha256(modified_input).digest()
        changed_hashes.append(changed_hash)

    return all(bit != original_hash[i] for changed_hash in changed_hashes for i, bit in enumerate(changed_hash))

if __name__ == "__main__":
    input_data = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    result = bit_change_test(input_data)
    if result:
        print("SHA-256 spełnia kryterium SAC")
    else:
        print("SHA-256 nie spełnia kryterium SAC")
