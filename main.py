
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


def vigenere_decrypt(ciphertext, key):
    alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    ciphertext = ciphertext.lower().replace("ё", "е").replace(" ", "")
    key = key.lower().replace("ё", "е").replace(" ", "")
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char not in alphabet:
            plaintext += char
        else:
            char_index = alphabet.index(char)
            key_char = key[key_index % len(key)]
            key_index += 1
            key_char_index = alphabet.index(key_char)
            plain_char_index = (char_index - key_char_index) % len(alphabet)
            plaintext += alphabet[plain_char_index]
    return plaintext

# Обслуговуючі функції
plaintext = input("Введіть текст для шифрування: ")
key = input("Введіть ключ: ")

# Шифрування
ciphertext = vigenere_encrypt(plaintext, key)
print("Зашифрований текст: ", ciphertext)

# Розшифрування
decrypted_plaintext = vigenere_decrypt(ciphertext, key)
print("Розшифрований текст: ", decrypted_plaintext)