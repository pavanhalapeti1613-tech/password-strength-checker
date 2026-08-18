# 🔐 Password Strength Checker

A Python-based password strength checker that evaluates passwords using multiple security criteria and allows passwords that meet the required strength threshold to proceed to **Argon2id hashing**.

## 🎯 Objective

The project evaluates password security and classifies passwords as:

* 🔴 Weak
* 🟡 Medium
* 🟢 Strong

It also provides feedback to help users create stronger passwords.

## ✨ Features

* Password length validation
* Uppercase letter detection
* Lowercase letter detection
* Number detection
* Special character detection
* Common password detection
* Repeated character detection
* Password strength scoring
* Gatekeeper validation
* Argon2id password hashing
* Feedback for improving weak or medium passwords

## 🛡️ Password Validation

The password is checked using six criteria:

1. **Length** — minimum 8 characters
2. **Uppercase** — at least one uppercase letter
3. **Lowercase** — at least one lowercase letter
4. **Number** — at least one digit
5. **Special character** — at least one special character
6. **Repeated characters** — avoids repeating the same character three or more times consecutively

### Strength Levels

| Score | Strength  | Gatekeeper |
| ----: | --------- | ---------- |
|   0–2 | 🔴 Weak   | ❌ Rejected |
|   3–5 | 🟡 Medium | ✅ Accepted |
|     6 | 🟢 Strong | ✅ Accepted |

Medium passwords receive improvement feedback but can still proceed to hashing.

## 🚪 Gatekeeper

The Gatekeeper controls whether a password proceeds to the hashing stage.

```text
Password
   ↓
Validation
   ↓
Strength Score
   ↓
┌───────────────┐
│   Gatekeeper  │
└───────┬───────┘
        │
   ┌────┴────┐
   ↓         ↓
Weak      Medium/Strong
   ↓         ↓
Reject    Argon2id
             ↓
          Hash
```

Weak passwords are rejected, while Medium and Strong passwords proceed to Argon2id hashing.

## 🔐 Argon2id Hashing

Passwords that pass the Gatekeeper are hashed using **Argon2id** through the `argon2-cffi` library.

The original password should never be stored as plain text.

Example hash format:

```text
$argon2id$v=19$m=65536,t=3,p=4$...
```

The hash contains information about the Argon2id parameters and a randomly generated salt.

## 🧰 Technologies Used

* Python
* Regular Expressions (`re`)
* Argon2id
* `argon2-cffi`
* Conditional statements
* String handling
* Sets

## 📦 Installation

### 1. Install Python

Download Python from:

https://www.python.org/downloads/

### 2. Install Argon2

Open the terminal and run:

```bash
python -m pip install argon2-cffi
```

### 3. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 4. Navigate to the Project

```bash
cd password-strength-checker
```

### 5. Run the Program

```bash
python password_checker.py
```

## 💻 Example

### Strong Password

```text
Enter your password: X7@mQ9#kLp2!

Password Strength Result
------------------------------
Strong Password
Score: 6/6

Password passed the Gatekeeper.

Password successfully hashed using Argon2id.
```

### Medium Password

```text
Enter your password: MyPassword12

Password Strength Result
------------------------------
Medium Password
Score: 5/6

Tips to make your password stronger:
- Add at least one special character.

Password passed the Gatekeeper.

Password successfully hashed using Argon2id.
```

### Weak Password

```text
Enter your password: abc

Password rejected by Gatekeeper.

Password will NOT be hashed.
```

### Common Password

```text
Enter your password: 123456

Common password detected!
Please choose a different password.
```

## 📁 Project Structure

```text
Password-Strength-Checker/
│
├── password_checker.py
└── README.md
```

## 🔒 Security Features

The project includes several security-focused checks:

* Common password detection
* Password complexity validation
* Repeated-character detection
* Minimum password length
* Strength scoring
* Gatekeeper validation
* Argon2id password hashing
* Feedback for improving password security

## 🚀 Future Improvements

* Add a larger common/breached-password database
* Add password entropy estimation
* Add a graphical user interface
* Add a visual password strength meter
* Add secure password verification
* Add database integration
* Add unit testing
* Detect keyboard patterns such as `qwerty` and `asdfgh`
* Detect sequential patterns such as `123456`
* Add configurable password policies

## 👨‍💻 Author

**Pavan V Halapeti**

Electronics and Communication Engineering Student

### Interests

* Cybersecurity
* Python
* Networking
* Artificial Intelligence
* Web Development

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐.
