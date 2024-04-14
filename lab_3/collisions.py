import hashlib

def find_collisions():
    # Tworzymy słownik, który będzie przechowywał skróty MD5 dla różnych tekstów
    hash_map = {}

    # Przechodzimy przez zakres od 0 do 2^12, czyli możliwe kombinacje pierwszych 12 bitów
    for i in range(2**12):
        # Tworzymy tekst na podstawie numeru w zakresie
        text = str(i)
        # Obliczamy skrót MD5 dla tego tekstu
        md5_hash = hashlib.md5(text.encode()).hexdigest()
        # Wybieramy pierwsze 12 bitów z tego skrótu
        first_12_bits = md5_hash[:3]  # Pierwsze 3 znaki reprezentujące 12 bitów
        # Sprawdzamy, czy ten zestaw pierwszych 12 bitów już istnieje w słowniku
        if first_12_bits in hash_map:
            # Jeśli istnieje, to mamy kolizję, więc drukujemy teksty, które dały kolizję
            print("Collision found for first 12 bits:", first_12_bits)
            print("Text 1:", hash_map[first_12_bits])
            print("Text 2:", text)
            print()
        else:
            # Jeśli nie istnieje, to dodajemy ten zestaw pierwszych 12 bitów do słownika
            hash_map[first_12_bits] = text

if __name__ == "__main__":
    find_collisions()
