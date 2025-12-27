import string

def load_common_passwords(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f)

common_passwords = load_common_passwords(r"C:\python\PYTHON PROJECTS\PROJECT1\seclist.txt")



def check_password_strength(password):
    if password in common_passwords:
        return "Weak (Common Password)"

    has_upper = has_lower = has_digit = has_special = False

    for ch in password:
        if ch in string.ascii_uppercase:
            has_upper = True
        elif ch in string.ascii_lowercase:
            has_lower = True
        elif ch in string.digits:
            has_digit = True
        elif ch in string.punctuation:
            has_special = True

    score = sum([
        has_upper,
        has_lower,
        has_digit,
        has_special,
        len(password) >= 8
    ])

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


password = input("Enter your password: ")
print("Password strength:", check_password_strength(password))
