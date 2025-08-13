import re

def check_password_complexity(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "Length (min 8 characters)": not length_error,
        "Contains lowercase letter": not lowercase_error,
        "Contains uppercase letter": not uppercase_error,
        "Contains digit": not digit_error,
        "Contains special character": not special_char_error
    }

    is_strong = all(errors.values())

    return is_strong, errors

if __name__ == "__main__":
    password = input("Enter your password: ")
    is_valid, result = check_password_complexity(password)

    if is_valid:
        print("Your password is strong.")
    else:
        print("Your password is weak. Issues:")
        for rule, passed in result.items():
            if not passed:
                print(f" - {rule}")
