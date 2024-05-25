import re
import string
from flask import Flask, request, render_template

app = Flask(__name__)


class PasswordStrengthTester:
    def __init__(self, dictionary_file):
        self.common_passwords = self.load_common_passwords(dictionary_file)

    def load_common_passwords(self, dictionary_file):
        with open(dictionary_file, "r") as file:
            common_passwords = [line.strip() for line in file]
        return common_passwords

    def test_password(self, password):
        score = 0
        feedback = []

        # Length score
        length = len(password)
        if length < 6:
            feedback.append("Password is too short. Minimum length is 6 characters.")
        elif length <= 8:
            score += 1
            feedback.append("Password length is acceptable but could be longer.")
        elif length <= 12:
            score += 2
            feedback.append("Password length is good.")
        else:
            score += 3
            feedback.append("Password length is excellent.")

        # Complexity score
        lower = any(c.islower() for c in password)
        upper = any(c.isupper() for c in password)
        digit = any(c.isdigit() for c in password)
        special = any(c in string.punctuation for c in password)

        if lower and upper and digit and special:
            score += 4
            feedback.append(
                "Password has a good mix of lowercase, uppercase, digits, and special characters."
            )
        elif lower and upper and digit:
            score += 3
            feedback.append(
                "Password has lowercase, uppercase, and digits. Adding special characters would improve strength."
            )
        elif lower and upper:
            score += 2
            feedback.append(
                "Password has both lowercase and uppercase letters. Adding digits and special characters would improve strength."
            )
        elif lower:
            score += 1
            feedback.append(
                "Password has only lowercase letters. Adding uppercase letters, digits, and special characters would significantly improve strength."
            )

        # Sequence score
        if re.search(r"(.)\1{2,}", password):
            feedback.append(
                "Password has sequences of repeated characters. Avoid using repeated sequences."
            )
        else:
            score += 1

        # Dictionary check
        if password.lower() in self.common_passwords:
            feedback.append("Password is too common. Avoid using common passwords.")
        else:
            score += 1

        # Determine strength level
        if score <= 3:
            strength_level = "Weak"
        elif score <= 6:
            strength_level = "Moderate"
        else:
            strength_level = "Strong"

        return {
            "password": password,
            "score": score,
            "strength": strength_level,
            "feedback": feedback,
        }


tester = PasswordStrengthTester("pass.csv")


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        password = request.form["password"]
        result = tester.test_password(password)
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
