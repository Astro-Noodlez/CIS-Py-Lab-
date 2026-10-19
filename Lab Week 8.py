

def vigenere_square(alpha):
    alpha = list(alpha)
    sq_list = [vg_header(alpha)]
    for i in range(len(alpha)):
        sq_list.append(list(alpha[i]) + alpha[i:] + alpha[:i])
    return sq_list


def vigenere_print(sq_list):
    for i, row in enumerate(sq_list):
        print(f'| {' | '.join(row)} |')
        if i == 0:
            print(f"{'|---'*len(row)}|")


def vg_header(alpha):
    return list(' ') + list(alpha)



def letter_to_index(letter, alpha):
    return alpha.find(letter)


def index_to_letter(index, alpha):
    if 0 <= index < len(alpha):
        return alpha[index]

def vigenere_index(key_letter, plaintext_letter, alpha):
    return index_to_letter(
        (letter_to_index(plaintext_letter, alpha) +
         letter_to_index(key_letter, alpha)) %
            len(alpha), alpha)





def anti_vg_index(key_letter, cipher_text, alpha):
    return index_to_letter(
        (letter_to_index(cipher_text, alpha) -
         letter_to_index(key_letter, alpha) + len(alpha)) %
          len(alpha), alpha)

def encrypt_vigenere(key, plaintext, alpha):
    cipher_text = []
    counter = 0
    for c in plaintext:
        if c == ' ':
            cipher_text.append(" ")
        elif c in alpha:
            cipher_text.append(vigenere_index(key[counter % len(key)], c, alpha))
            counter += 1
    return ''.join(cipher_text)

def decrypt_vigenere(key, cipher_text, alpha):
    plaintext = []
    counter = 0
    for c in cipher_text:
        if c == ' ':
            plaintext.append(" ")
        elif c in alpha:
            plaintext.append(anti_vg_index(key[counter % len(key)], c, alpha))
            counter += 1
    return ''.join(plaintext)

def enc_menu(key, alpha, encrypted_list):
    plaintext = input("Enter the text you'd like to encrypt: ")
    encrypted_list.append(encrypt_vigenere(key, plaintext, alpha))

def dec_menu(key, alpha, encrypted_list):
    for cipher_text in encrypted_list:
        print(decrypt_vigenere(key, cipher_text, alpha))

def dec_dump_menu(encrypted_list):
    for cipher_text in encrypted_list:
        print(cipher_text)



def main():
    key = 'GEOPHYSICS'
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVQXYZabcdefghijklmnopqrstuvwxyz'
    # message = 'Pandas are awesome'
    encrypted_list = []

    menu = [
        ['1). Encrypt', enc_menu, [key, alpha, encrypted_list]],
        ['2). Decrypt', dec_menu, [key, alpha, encrypted_list]],
        ['3). Dump Decrypt', dec_dump_menu, [encrypted_list]],
        ['4). Quit', exit, [0]]
    ]
    while True:
        print("-"*80)
        for menu_item in menu:
            print(menu_item[0])
        try:
            choice = int(input("Make your choice: "))
            if not (0 < choice <= len(menu)):
                print("Improper choice")
            else:
                menu[choice-1][1](*menu[choice-1][2])
        except ValueError as ignored:
            print("Improper choice, you must enter an integer between 1 and 4")

if __name__ == '__main__':
    main()


alpha = 'ABCDEFGHIJKLMNOPQRSTUVQXYZabcdefghijklmnopqrstuvwxyz'
key = 'GEOPHYSICS'
message = 'Pandas are awesome'
# vigenere_print(vigenere_square(alpha))
# print(vigenere_index('h','p', alpha))
ct = encrypt_vigenere(key, message, alpha)

# print(ct)
# print(encrypt_vigenere(key, message, alpha))
# print(decrypt_vigenere(key, ct, alpha))