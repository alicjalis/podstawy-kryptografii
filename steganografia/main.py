from PIL import Image


def text_to_binary(text):
    binary = ''.join(format(ord(char), '08b') for char in text)
    binary += '00000000'  # znacznik konca

    return binary


def binary_to_text(binary_str):
    binary_chunks = []
    chunk_size = 8

    for i in range(0, len(binary_str), chunk_size):
        chunk = binary_str[i:i + chunk_size]
        binary_chunks.append(chunk)

    text = ''
    for chunk in binary_chunks:
        text += chr(int(chunk, 2))
    return text


def encode_text(message, image, path):
    message_bin = text_to_binary(message)

    img = Image.open(image)
    width, height = img.size
    pixels = width*height
    if len(message_bin) > pixels * 3 - 2:
        print("Wiadomość jest za długa")

    data_index = 0
    encoded_pixels = img.load()

    for y in range(height):
        for x in range(width):
            r, g, b = encoded_pixels[x, y]

            # wyzerowanie najmniej znaczacego bitu
            r &= 0b11111110
            # ustawienie najmniej znaczacego bitu na 1/0
            r |= int(message_bin[data_index])
            data_index += 1

            if data_index >= len(message_bin):
                encoded_pixels[x, y] = (r, g, b)
                img.save(path)
                return

            # wyzerowanie najmniej znaczacego bitu
            g &= 0b11111110
            # ustawienie najmniej znaczacego bitu na 1/0
            g |= int(message_bin[data_index])
            data_index += 1

            if data_index >= len(message_bin):
                encoded_pixels[x, y] = (r, g, b)
                img.save(path)
                return

            # wyzerowanie najmniej znaczacego bitu
            b &= 0b11111110
            # ustawienie najmniej znaczacego bitu na 1/0
            b |= int(message_bin[data_index])
            data_index += 1

            if data_index >= len(message_bin):
                encoded_pixels[x, y] = (r, g, b)
                img.save(path)
                return

            encoded_pixels[x, y] = (r, g, b)

    img.save(path)


def decode_text(path):
    img = Image.open(path)
    width, height = img.size
    encoded_pixels = img.load()

    binary_text = ''

    for y in range(height):
        for x in range(width):
            r, g, b = encoded_pixels[x, y]

            binary_text += str(1 & r)
            if binary_text[-8:] == '00000000':  # znacznik końca tekstu
                binary_text = binary_text[:-8]

                return binary_to_text(binary_text)

            binary_text += str(1 & g)
            if binary_text[-8:] == '00000000':  # znacznik końca tekstu
                binary_text = binary_text[:-8]

                return binary_to_text(binary_text)

            binary_text += str(1 & b)
            if binary_text[-8:] == '00000000':  # znacznik końca tekstu
                binary_text = binary_text[:-8]

                return binary_to_text(binary_text)

    return "Nie ma ukrytego tekstu w obrazie"


def main():
    message = "Tajna wiadomosc"
    image = "pies.png"
    encoded_image = "tajny_obraz.png"

    encode_text(message, image, encoded_image)

    print(decode_text(encoded_image))

    return


if __name__ == "__main__":
    main()
