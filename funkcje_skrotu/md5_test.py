import hashlib

def generate_md5_hash(input_text):
    return hashlib.md5(input_text.encode()).hexdigest()

# Example usage:
input_text = "tren"
md5_hash = generate_md5_hash(input_text)
print("MD5 Hash:", md5_hash)
