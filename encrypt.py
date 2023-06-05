def vigenere_encrypt(plaintext, key):
    alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    plaintext = plaintext.lower().replace("ё", "е").replace(" ", "")
    key = key.lower().replace("ё", "е").replace(" ", "")
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char not in alphabet:
            ciphertext += char
        else:
            char_index = alphabet.index(char)
            key_char = key[key_index % len(key)]
            key_index += 1
            key_char_index = alphabet.index(key_char)
            cipher_char_index = (char_index + key_char_index) % len(alphabet)
            ciphertext += alphabet[cipher_char_index]
    return ciphertext


plaintext = input("Введіть текст для шифрування: ")
key = input("Введіть ключ: ")


ciphertext = vigenere_encrypt(plaintext, key)
print("Зашифрований текст: ", ciphertext)

