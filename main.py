import os
import sys
import base64

# use pycryptodome
from Crypto.Cipher import AES
from pwnlib.term.readline import raw_input

# Global variables
key = os.urandom(16) #not random
flag = "rhitCTF{this_is_a_flag}"
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

# Main function
def main(iv):
    print ("Welcome to the AES cipher challenge!")
    user_input1 = raw_input("Please enter your name:")
    iv = iv+user_input1
    user_input2 = raw_input("What is your major: ")
    iv = iv+user_input2
    user_input3 = raw_input("Enter the key: ")
    print(encrypt_flag())
    if check_user_input(user_input3):
        print ("You got the flag!")
    else:
        print ("Wrong flag!")
    sys.exit(0)

if __name__ == "__main__":
    main(iv)
