#ROT13 Cipher
#Objctive:  Shift individual letters to the right by 13 places in the alphabet

# import string
# alphabet = string.ascii_lowercase

# cipher_input = str(input("Input:    "))
# print(f'This is the input:    {cipher_input}')

# for x in cipher_input:
#     b = alphabet.find(x)
#     i = (b + 13)%26
#     print(f'Value of i,    {i}')
# cipher_output = cipher_input.replace(x,alphabet[i])



# print(f'This is the output:    {cipher_output}')

###Below is the solution taken from the ceaser cipher Mr Arold sent me back in September
# Annotate it and figure out why it works the way it does
import string
alphabet = string.ascii_lowercase
o = str(input("Input text to encrypt: "))

def encrypt(shift, plaintext):
    ciphertext = ''

    for eachletter in plaintext.lower():
        try:
            i = (alphabet.index(eachletter) + shift) % 26
            ciphertext += alphabet[i]
        except:
            ciphertext += eachletter

    return ciphertext.lower()

print(encrypt(12, o))