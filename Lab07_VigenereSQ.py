"""Lab 07 Week 7!
Live long, and prosper"""

def vigenere_header(alpha):
    alpha_len = len(alpha)
    print("|CYP", end='')
    for i in range(alpha_len):
        print(f"| {alpha[i % alpha_len]}", end=' ')
    print("|")
    print(f"{'|---'*((alpha_len) + 1)}|")

def vigenere_sq(alpha):
    alpha_len = len(alpha)
    vigenere_header(alpha)
    for shift in range(alpha_len):
        for i in range (alpha_len):
            if i == 0:
                w = alpha[(i + shift) % alpha_len]
                print(f"| {w}", end=' ')
                print(f"| {w}", end=' ')
            else:
                print(f"| {alpha[(i + shift) % alpha_len]}", end=' ')
        print('|')



def letter_to_index(letter, alpha:str):
    return alpha.lower().index(letter.lower())

def index_to_letter(index, alpha):
    if 0 <= index < len(alpha):
        return alpha[index]
    return ''

def vigenere_index(key_letter, plaintext_letter, alpha):
    return ((letter_to_index(key_letter, alpha) +
            letter_to_index(plaintext_letter, alpha)) %
            len(alpha))



def encrypt_vigenere(key, plaintext, alphabet):
    cipher_text = ''
    counter = 0
    for c in plaintext:
        if c == ' ':
            cipher_text += ' '
        elif(c.upper() in alpha):
            cipher_text += index_to_letter(
                vigenere_index(key[counter % len(key)], c, alpha), alpha)
            counter += 1
    return cipher_text


key = 'GEOPHYSICS'
message = 'TODAY IS A GOOD DAY TO DIE'
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# vigenere_sq(alpha)
# print(letter_to_index('h', alpha))
# print(index_to_letter(7, alpha))
# print(index_to_letter(
#     vigenere_index("B","Z", alpha), alpha))

print(encrypt_vigenere(key, message, alpha))


#STUFF FOR LATER#

# def letter_to_index(letter, alpha:str):
#     for i, l in enumerate(alpha):
#         if l == letter:
#             return i