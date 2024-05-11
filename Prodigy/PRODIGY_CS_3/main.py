import os
import re
import time
import platform
import colorama
import random
import string
from colorama import Fore, Style

# Initialize colorama
colorama.init(autoreset=True)

# Function to clear screen
def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")

# Initilize logo
logo = f'''
{Fore.GREEN} ____        _  __ _ _   _            _
{Fore.RED}/ ___|  __ _| |/ _(_) | | | __ _  ___| | _____ _ __
{Fore.CYAN}\___ \ / _` | | |_| | |_| |/ _` |/ __| |/ / _ \ '__|
{Fore.YELLOW} ___) | (_| | |  _| |  _  | (_| | (__|   <  __/ |
{Fore.BLUE}|____/ \__,_|_|_| |_|_| |_|\__,_|\___|_|\_\___|_|
{Fore.MAGENTA}
'''

# Function to display logo with delay
def display_logo_with_delay(logo_text, delay=0.1):
    clear_screen()
    for line in logo_text.split('\n'):
        print(line)
        time.sleep(delay)

# Function to get user choice
def get_user_choice():
    while True:
        display_logo_with_delay(logo)
        print(Fore.RED + "\n[+]" + Fore.GREEN + "What would you like to do?")
        print(Fore.GREEN + "[1] " + Fore.RED + "Check password strength")
        print(Fore.GREEN + "[2] " + Fore.RED + "Generate random password")
        print(Fore.GREEN + "[3] " + Fore.RED + "Exit")
        choice = input(Fore.RED + "[+] Enter your choice (1-3): " + Fore.BLUE)
        if choice in ['1', '2', '3']:
            return choice
        else:
            print(Fore.RED + "[+]" + Fore.GREEN + "Invalid choice." + Fore.BLUE + "Please enter a number between 1 and 3.")

# Function to check password strength
def check_password_strength(password, rules):
    feedback = []
    for rule_key, (rule_pattern, rule_message) in rules.items():
        if not re.search(rule_pattern, password):
            feedback.append(rule_message)
    return feedback or ["Strong"]

# Function to generate random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Main function
# Main function
def main():
    rules = {
        'min_length': (r".{8,}", "Password should be at least 8 characters long."),
        'min_uppercase': (r"[A-Z]", "Password should include at least one uppercase letter."),
        'min_lowercase': (r"[a-z]", "Password should include at least one lowercase letter."),
        'min_digits': (r"\d", "Password should include at least one digit."),
        'min_special_chars': (r"[_@$#%^&*!]", "Password should include at least one special character (_@$#%^&*!)."),
        'disallowed_patterns': (r"password|123", "Password should not contain 'password' or '123'.")
    }

    display_logo_with_delay(logo)
    print(Style.BRIGHT + Fore.MAGENTA + "\n\n\t[+]" + Fore.RED + " Welcome to Advanced Password Strength Checker!")
    input()

    while True:
        choice = get_user_choice()
        display_logo_with_delay(logo, 0)

        if choice == '1':
            password = input(Fore.RED + "[+]" + Fore.GREEN + " Enter the password to check: " + Fore.BLUE)
            feedback = check_password_strength(password, rules)
            print(Fore.BLUE + "[+]" + Fore.GREEN + " Your password strength is: " + Fore.RED + " ".join(feedback))
            input()
            
        elif choice == '2':
            generated_password = generate_password()
            print(Fore.BLUE + "[+]" + Fore.GREEN + f" Generated password: {generated_password}")
            input()
            
        elif choice == '3':
            print(Fore.YELLOW + "[+]" + Fore.BLUE + "Exiting the program. Goodbye!")
            break

    

if __name__ == "__main__":
    main()
