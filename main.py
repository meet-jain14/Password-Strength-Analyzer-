import re

def evaluate_password_strength(password):
    strength = {
        "length": False,
        "uppercase": False,
        "lowercase": False,
        "digits": False,
        "special": False,
    }
    if len(password) >= 12:
        strength["length"] = True

    if re.search(r'[A-Z]', password):
        strength["uppercase"] = True

    if re.search(r'[a-z]', password):
        strength["lowercase"] = True

    if re.search(r'[0-9]', password):
        strength["digits"] = True

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength["special"] = True
    return strength

def get_suggestions(strength):
    suggestions = []
    if not strength["length"]:
        suggestions.append("Increase the password length to at least 12 characters.")
    if not strength["uppercase"]:
        suggestions.append("Add at least one uppercase letter.")
    if not strength["lowercase"]:
        suggestions.append("Add at least one lowercase letter.")
    if not strength["digits"]:
        suggestions.append("Include at least one digit.")
    if not strength["special"]:
        suggestions.append("Use at least one special character (e.g., !, @, #, $).")
    return suggestions
def main():
    password = input("Enter a password to evaluate: ")
    strength = evaluate_password_strength(password)
    
    if all(strength.values()):
        print("Your password is strong.")
    else:
        print("Your password is weak. Here are some suggestions to improve it:")
        suggestions = get_suggestions(strength)
        for suggestion in suggestions:
            print(f"- {suggestion}")
if __name__ == "__main__":
    main()