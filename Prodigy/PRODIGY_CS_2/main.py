import os
import platform
import time
from PIL import Image
import colorama
from colorama import Fore, Style

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

def encrypt_image(image_path, key):
    try:
        img = Image.open(image_path)
    except IOError:
        print(Fore.RED + "[-] Error: Failed to open image.")
        return

    if not isinstance(key, int):
        print(Fore.RED + "[-] Error: Key must be an integer.")
        return

    encrypted_img = Image.new('RGB', img.size)
    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = img.getpixel((i, j))
            encrypted_img.putpixel((i, j), (r^key, g^key, b^key))

    encrypted_img.save("encrypted_" + image_path.split(".")[0] + ".png", 'PNG')
    print(Fore.BLUE + "[+]" + Fore.GREEN + " Encrypted image saved as: " + Fore.RED + "encrypted_" + image_path.split(".")[0] + ".png")

def decrypt_image(image_path, key):
    try:
        img = Image.open(image_path)
    except IOError:
        print(Fore.RED + "[-] Error: Failed to open image.")
        return

    if not isinstance(key, int):
        print(Fore.RED + "[-] Error: Key must be an integer.")
        return

    decrypted_img = Image.new('RGB', img.size)
    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = img.getpixel((i, j))
            decrypted_img.putpixel((i, j), (r^key, g^key, b^key))

    decrypted_img.save("decrypted_" + image_path.split(".")[0] + ".png", 'PNG')
    print(Fore.BLUE + "[+]" + Fore.GREEN + " Decrypted image saved as: " + Fore.RED + "decrypted_" + image_path.split(".")[0] + ".png")



# Main Function
def main():
    salfi_hackers_logo(logo)
    print(Style.BRIGHT + Fore.MAGENTA + "\n\n\t[+]" + Fore.RED + " Welcome to Image Encryption!")
    input()
    while True:
        salfi_hackers_logo(logo)
        print(Fore.RED + "\n[+]" + Fore.GREEN + "What would you like to do?")
        print(Fore.GREEN + "[1] " + Fore.RED + "Encrypt an image")
        print(Fore.GREEN +  "[2] " + Fore.RED + "Decrypt an image")
        print(Fore.GREEN +  "[3] " + Fore.RED + "Exit")

        choice = input(Fore.RED + "[+] Enter your choice (1-3): " + Fore.BLUE)

        if choice == '1':
            image_path = input(Fore.RED + "[+]" + Fore.GREEN + " Enter the path to the image to encrypt: " + Fore.BLUE)
            key = int(input(Fore.RED + "[+]" + Fore.GREEN + " Enter the encryption key (an integer): " + Fore.BLUE))
            encrypt_image(image_path, key)
        elif choice == '2':
            image_path = input(Fore.RED + "[+]" + Fore.GREEN + " Enter the path to the image to decrypt: " + Fore.BLUE)
            key = int(input(Fore.RED + "[+]" + Fore.GREEN + " Enter the decryption key (an integer): " + Fore.BLUE))
            decrypt_image(image_path, key)
        elif choice == '3':
            print(Fore.YELLOW + "[+]" + Fore.BLUE + "Exiting the program. Goodbye!")
            break
        else:
            print(Fore.RED + "[+]" + Fore.GREEN + "Invalid choice." + Fore.BLUE + "Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
