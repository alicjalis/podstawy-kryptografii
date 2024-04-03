import hashlib

def generate_hashes(input_text):
    results = {}

    # MD5
    md5_hash = hashlib.md5()
    md5_hash.update(input_text.encode())
    results['MD5'] = md5_hash.hexdigest()

    # SHA-1
    sha1_hash = hashlib.sha1()
    sha1_hash.update(input_text.encode())
    results['SHA-1'] = sha1_hash.hexdigest()

    # SHA-2 variants (SHA-224, SHA-256, SHA-384, SHA-512)
    sha2_variants = ['sha224', 'sha256', 'sha384', 'sha512']
    for variant in sha2_variants:
        sha2_hash = hashlib.new(variant)
        sha2_hash.update(input_text.encode())
        results[variant.upper()] = sha2_hash.hexdigest()

    return results

def main():
    input_text = input("Podaj tekst do zaszyfrowania: ")
    hashes = generate_hashes(input_text)

    print("\nWartości skrótów:")
    for algorithm, value in hashes.items():
        print(f"{algorithm}: {value}")

if __name__ == "__main__":
    main()
