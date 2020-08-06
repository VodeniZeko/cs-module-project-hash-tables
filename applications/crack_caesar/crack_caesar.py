
import re

frequency_of_english_letters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
                                'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']


def find_cipher(string):
    total = 0
    table = {}
    seed = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for c in seed:
        table[c] = 1
    for c in string:
        if re.match(r'[A-Z]', c):
            table[c] += 1
            total += 1
    sorted_letter_occurences = [entry[0] for entry in sorted(
        table.items(), key=lambda x: x[1], reverse=True)]
    cipher = {}
    index = 0
    for letter in sorted_letter_occurences:
        cipher[letter] = frequency_of_english_letters[index]
        index += 1
    return cipher


def decode_string(string, cipher):
    new_string = ''
    for c in string:
        if re.match(r'[A-Z]', c):
            new_string = new_string + cipher[c]
        else:
            new_string = new_string + c
    return new_string


f_in = open('ciphertext.txt', 'r')
encrypted_text = f_in.read()

cipher = find_cipher(encrypted_text)

decoded_text = decode_string(encrypted_text, cipher)

f_out = open('decodedtext.txt', 'w')
f_out.write(decoded_text)
