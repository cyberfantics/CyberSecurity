# Password Strength Tester

## Overview

The Password Strength Tester is a web application designed to evaluate the strength of user-entered passwords. It provides feedback based on various criteria such as length, complexity, and common patterns to help users create more secure passwords.

## Features

### Password Strength Evaluation

The application evaluates the strength of a password based on several factors:

1. **Length**:
   - Less than 6 characters: Password is too short.
   - 6 to 8 characters: Password length is acceptable but could be longer.
   - 8 to 12 characters: Password length is good.
   - More than 12 characters: Password length is excellent.

2. **Complexity**:
   - Checks for the presence of lowercase letters, uppercase letters, digits, and special characters.
   - Provides feedback on the mix of character types.

3. **Character Repetition**:
   - Identifies sequences of repeated characters and provides feedback to avoid such patterns.

4. **Common Passwords**:
   - Checks the password against a list of common passwords and advises against using them.

### User Interface

- **Form Handling**:
  - The form allows users to enter a password and submit it for evaluation.
  - On page load, the form is cleared, and any previous result is hidden.

- **Result Display**:
  - The result section displays the password, score, strength level, and specific feedback.
  - Strength levels are categorized as Weak, Moderate, or Strong.
  - Feedback is provided in a user-friendly format, helping users understand how to improve their passwords.

### Technologies Used

- **Flask**: A lightweight WSGI web application framework in Python used to build the server-side logic.
- **HTML/CSS**: For structuring and styling the web pages.
- **JavaScript**: For enhancing the interactivity of the application, such as hiding results when needed.
- **Python**: For the backend logic to evaluate the password strength.

### Files Included

- **app.py**: The main Flask application file containing the server-side logic.
- **templates/index.html**: The HTML template for the main page.
- **static/style.css**: The CSS file for styling the application.
- **static/script.js**: The JavaScript file for client-side interactions.
- **pass.csv**: A file containing a list of common passwords used to check against user-entered passwords.

### Usage

1. Open the application in a web browser after running `python app.py`.
2. Enter a password in the provided form and submit it.
3. The application will display the password strength, a score, and feedback on how to improve the password.

### Demo Video

[![Watch the demo video](https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg)](https://www.linkedin.com/posts/mansoor-bukhari-77549a264_cybersecurity-growintern-internshipjourney-activity-7200205522204053504-Lzh1?utm_source=li_share&utm_content=feedcontent&utm_medium=g_dt_web&utm_campaign=copy)

### Developer

Syed Mansoor ul Hassan Bukhari
