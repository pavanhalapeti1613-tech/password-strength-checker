import re
from argon2 import PasswordHasher

ph = PasswordHasher()
common_passwords = {
    "123456","123456789","qwerty","12345678","111111","1234567890","1234567","password","123123","987654321","qwertyuiop","mynoob","123321","666666","18atcskd2w","7777777","1q2w3e4r","654321","555555","3rjs1la7qe","google","1q2w3e4r5t","123qwe","zxcvbnm","1q2w3e","######","$$$$$$","iloveyou","0987654321","asdfghjkl","qpwoeiru",
}

def check_password_strength(password):
    score = 0
    feedback = []

    # Check for common password
    if password.lower() in common_passwords:
        print("Common password detected!")
        print("Please choose a different password.")
        return False

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
        print("The password may undergo a brute-force attack.")
        return False

    # Check uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check number
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Check special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Check repetition of characters
    if re.search(r"(.)\1{2,}", password):
        feedback.append("Avoid repeating the same character 3 or more times.")
    else:
        score += 1

    # Display result
    print("\nPassword Strength Result")
    print("-" * 30)

    if score == 6:
        print("Strong Password")
    elif score >= 3:
        print("Medium Password")
    else:
        print("Weak Password")

    print(f"Score: {score}/6")

    # Show feedback for Medium/Weak passwords
    if feedback:
        print("\nTips to make your password stronger:")
        for item in feedback:
            print("-", item)

    # Gatekeeper decision
    if score >= 3:
        print("\nPassword passed the Gatekeeper.")
        return True
    else:
        print("\nPassword rejected by Gatekeeper.")
        return False
    
# Main Program
password = input("Enter your password: ")

if check_password_strength(password):

    print("\nPassword is ready for secure hashing with Argon2id.")

    hashed_password = ph.hash(password)

    print("Password successfully hashed using Argon2id.")
    print("Hash:", hashed_password)

else:
    print("\nPassword will NOT be hashed.")