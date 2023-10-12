import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

def morse_code(text):
    # Your morse code function (unchanged)
    morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
             'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
             'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
             'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
             'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
             'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
             '4': '....-', '5': '.....', '6': '-....', '7': '--...',
             '8': '---..', '9': '----.', '0': '-----', ' ': '/'}
    morse_code = ""
    for char in text:
        if char.upper() in morse:
            morse_code += morse[char.upper()] + ' '
    return morse_code

# Generate a random 16-byte AES key
key = os.urandom(16)
cipher = AES.new(key, AES.MODE_CBC)
flag = 'rhit{this_is_the_flag}'

# Take user input
user_input = input("Hey! I can help you encript thing! What do you want encripted: ")

# Pad the user input to the block size (16 bytes for AES)
padded_user_input = pad(user_input.encode('utf-8'), 16)
padded_flag = pad(flag.encode('utf-8'), 16)

# Encrypt the padded user input
ciphertext = cipher.encrypt(padded_user_input)
cipherflag = cipher.encrypt(padded_flag)

# Convert the ciphertext to Morse code
morse_text = morse_code(base64.b64encode(ciphertext).decode('utf-8'))
morse_flag = morse_code(base64.b64encode(cipherflag).decode('utf-8'))

#print("AES Key:", key)
#print("Cypertext:", base64.b64encode(ciphertext).decode('utf-8'))
#print("Cyperflag:", base64.b64encode(cipherflag).decode('utf-8'))
print("Here you go:", morse_text)
print("Oh and can you figure out what this is for me:", morse_flag)

user_input2 = input("Do you know what the flag is: ")
if user_input2 == flag:
    print("Yay! You found the flag! I was wondering were it went!")

else:
    print("Boo, that is not want I am looking for!")