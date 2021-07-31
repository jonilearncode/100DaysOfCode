"""
Program: caesar-cypher
Description: A UI for cypher plain text messages with
Caesar Cypher method.
Author: Joao Teixeira
Date: 2021.07
Version: 1.202107
"""

# Globals
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]

# Aux methods
def encrypt(plain_text, alphabet, shifted_alphabet):
    to_encrypt = list(plain_text)
    cypher = []
    for c in to_encrypt:
        # Catch ponctuation
        if not c in alphabet:
            cypher.append(c)
        else:
            index = alphabet.index(c)
            cypher.append(shifted_alphabet[index])
    return ''.join(cypher)

def decrypt(cypher, key, alphabet):
    r_key = len(alphabet) - key
    plain_text = encrypt(cypher, alphabet, shift_alphabet(r_key, alphabet))
    return ''.join(plain_text)


def shift_alphabet(key, alphabet):
    shifted = alphabet.copy()
    for i in range(key):
        shifted.pop(0)
        shifted.append(alphabet[i])
    return shifted

# Intro
print("Welcome to Caesar Cypher machine.")
while True:
    shifted_alphabet = []
    plain_text = ''
    cypher = ''
    # Select mode: 'encode' 'decode'
    encryption_type = input('Type "encode" to encrypt or "decode" to decrypt: ').lower()
    # Select key
    key = int(input('Enter a key as a number: '))
    assert encryption_type == "encode" or encryption_type == "decode"
    shifted_alphabet = shift_alphabet(key, alphabet)
    if encryption_type == "encode":
        plain_text = input(f'Type the message you want encrypt using only 26 letter alphabet [key={key}]: ').lower()
        # encrypt
        print(encrypt(plain_text, alphabet, shifted_alphabet))
    elif encryption_type == "decode":
        cypher = input(f'Type the cypher you want decrypt using only 26 letter alphabet [key={key}]: ').lower()
        # decrypt
        print(decrypt(cypher, key, alphabet))

    exit_program = input('\nType "y" to encrypt/decrypt again. Type anything else for "quit" ... ' )
    if exit_program == 'y':
        continue
    else:
        print(" Goodbye! ")
        break




