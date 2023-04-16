from utilis import alphabet1, alphabet2, little, rus, numeric


def shift(char, number):
    size = 26
    if rus(char):
        size = 33
    if little(char):
        add = (alphabet1.index(char) + number) % size
    else:
        add = (alphabet2.index(char) + number) % size
        return alphabet2[add]
    return alphabet1[add]


def caeser_encrypt(plaintext: str, key: int, flag=1):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            ciphertext += shift(char, key * flag)
        else:
            ciphertext += char
    return ciphertext


def viginer_encrypt(plaintext: str, key: str, flag=1):
    item = 0
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            ciphertext += shift(char, numeric(key[item % (len(key))]) * flag)
            item += 1
        else:
            ciphertext += char
    return ciphertext


def bodo(char):
    return bin(ord(char))


def vernam_shift(char_1, char_2):
    return chr(ord(char_1) ^ ord(char_2))


def vernam_encrypt(plaintext: str, key: str):
    item = 0
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            ciphertext += vernam_shift(char, (key[item % (len(key))]))
            item += 1
        else:
            ciphertext += char
    return ciphertext
