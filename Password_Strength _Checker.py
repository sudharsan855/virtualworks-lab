import re
def check_password(password):
    score = 0

    # Check password constraints and score
    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"[0-9]", password):
        score += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Check score to show password strength
    if score <= 2:
        print("Password Strength: Weak")
        print("Suggestion: Use at least 8 characters, including uppercase, lowercase, numbers, and special characters.")
        
    elif score == 3 or score == 4:
        print("Password Strength: Moderate")
        print("Suggestion: Add more character variety to make the password stronger.")

    else:
        print("Password Strength: Strong")
        print("Excellent! Your password is strong.")

password = input("Enter a password: ")
check_password(password)