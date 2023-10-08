import os
import sys
import base64

# use pycryptodome
from Crypto.Cipher import AES
from pwnlib.term.readline import raw_input

# Global variables
key = os.urandom(16) #not random
flag = "rhitCTF{thisistheflagforthischallenge}" #not the real flag
iv = None #using user input to create the initaial varible

# Encrypt the flag
def encrypt_flag():
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(cipher.encrypt(flag))

# Encrypt the user input
def encrypt_user_input(user_input):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(cipher.encrypt(user_input))

# Check if the user input is correct
def check_user_input(user_input):
    if encrypt_user_input(user_input) == key:
        return True
    else:
        return False

# write a function that will take a string input and translate it to morse code
def morse_code(user_input):
    morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
             'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
             'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
             'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
             'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
             'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
             '4': '....-', '5': '.....', '6': '-....', '7': '--...',
             '8': '---..', '9': '----.', '0': '-----', ', ': '--..--',
             '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
             '(': '-.--.', ')': '-.--.-'}
    morsecode = ""
    for letter in user_input:
        morsecode += morse[letter.upper()] + ' '
    return morsecode
# Main function
def main(iv):
    print ("Welcome to the AES cipher challenge!")
    user_input1 = raw_input("Please enter your name:")
    iv = iv+user_input1
    user_input2 = raw_input("What is your major: ")
    iv = iv+user_input2
    print(".... .. / .. - .----. ... / -. .. -.-. . / - --- / -- . . - / -.-- --- ..- / " + morse_code(encrypt_user_input(user_input1)))
    print(".. - .----. ... / ... --- / -.-. --- --- .-.. / - .... .- - / -.-- --- ..- / -- .- .--- --- .-. / .. -. /" + morse_code(encrypt_user_input(user_input2)))
    print(".--- ..- ... - / -... . -.-. .- ..- ... . / .. / .-.. .. -.- . / -.-- --- ..- / .... . .-. . / .. ... / - .... . / -.- . -.--" + morse_code(encrypt_flag()))
    user_input3 = raw_input("Enter the key: ")
    print(encrypt_flag())
    if check_user_input(user_input3):
        print ("You got the flag!")
    else:
        print ("Wrong flag!")
    sys.exit(0)

if __name__ == "__main__":
    main(iv)
