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


plaintext = input("Введіть зашифрований текст: ")
key = input("Введіть ключ: ")


decrypted_plaintext = vigenere_decrypt(plaintext, key)
print("Розшифрований текст: ", decrypted_plaintext)