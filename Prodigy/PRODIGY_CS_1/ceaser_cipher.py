import colorama
from colorama import Fore, Style
import os
import platform
import time
import sys
import re

# Initialize colorama
colorama.init(autoreset=True)

# Clear Screen Function
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def salfi_hackers_logo(n):
    clear_screen()
    for line in n.split('\n'):
        print(line)
        time.sleep(0.1)
        
logo = f'''
{Fore.GREEN} ____        _  __ _ _   _            _             
{Fore.RED}/ ___|  __ _| |/ _(_) | | | __ _  ___| | _____ _ __ 
{Fore.CYAN}\___ \ / _` | | |_| | |_| |/ _` |/ __| |/ / _ \ '__|
{Fore.YELLOW} ___) | (_| | |  _| |  _  | (_| | (__|   <  __/ |   
{Fore.BLUE}|____/ \__,_|_|_| |_|_| |_|\__,_|\___|_|\_\___|_|   
{Fore.MAGENTA}                                                    
'''

# Caesar Cipher Functions
def caesar_cipher(text, shift, decrypt=False):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                alphabet = 'abcdefghijklmnopqrstuvwxyz'
            else:
                alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            shifted_index = (alphabet.index(char) - shift) % 26 if decrypt else (alphabet.index(char) + shift) % 26
            encrypted_text += alphabet[shifted_index]
        else:
            encrypted_text += char
    return encrypted_text

def encrypt_message():
    salfi_hackers_logo(logo)
    message = input(Fore.RED + "[+]" + Fore.GREEN + " Enter the message to encrypt: " + Fore.BLUE)
    shift = int(input(Fore.RED + "[+]" + Fore.GREEN + " Enter the shift value (an integer): " + Fore.BLUE)) 
    encrypted_message = caesar_cipher(message, shift)
    print(Fore.BLUE + "[+]" + Fore.GREEN + " Encrypted message: " + Fore.RED + encrypted_message)
    input()
    
def decrypt_message():
    salfi_hackers_logo(logo)
    message = input(Fore.RED + "[+]" + Fore.GREEN + " Enter the message to decrypt: " + Fore.BLUE)
    shift = int(input(Fore.RED + "[+]" + Fore.GREEN + " Enter the shift value (an integer): " + Fore.BLUE))
    decrypted_message = caesar_cipher(message, shift, decrypt=True)
    print(Fore.BLUE + "[+]" + Fore.GREEN + " Encrypted Message: " + Fore.RED + decrypted_message + Fore.BLUE)
    input()
    

# Caesar Cipher Main Function
def main():
    salfi_hackers_logo(logo)
    print(Style.BRIGHT + Fore.MAGENTA + "\n\n\t[+]" + Fore.RED + " Welcome to Caesar Cipher!")
    input()
    while True:
        salfi_hackers_logo(logo)
        print(Fore.RED + "\n[+]" + Fore.GREEN + "What would you like to do?")
        print(Fore.GREEN + "[1] " + Fore.RED + "Encrypt a message")
        print(Fore.GREEN +  "[2] " + Fore.RED + "Decrypt a message")
        print(Fore.GREEN +  "[3] " + Fore.RED + "About")
        print(Fore.GREEN +  "[4] " + Fore.RED + "Exit")

        choice = input(Fore.RED + "[+] Enter your choice (1-4): " + Fore.BLUE)

        if choice == '1':
            encrypt_message()
        elif choice == '2':
            decrypt_message()
        elif choice == '3':
            about()
        elif choice == '4':
            print(Fore.YELLOW + "[+]" + Fore.BLUE + "Exiting the program. Goodbye!")
            break
        else:
            print(Fore.RED + "[+]" + Fore.GREEN + "Invalid choice." + Fore.BLUE + "Please enter a number between 1 and 4.")

# About Function
def about():
    salfi_hackers_logo(logo)
    print(Fore.GREEN + "Caesar Cipher")
    print(Fore.RED + "This program encrypts and decrypts messages using the Caesar Cipher.")
    print(Fore.RED + "Developed by Salfi Hackers")
    input()

if __name__ == "__main__":
    main()
