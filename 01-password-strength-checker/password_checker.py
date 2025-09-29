import string
"""
Things to focus on:
- Length: longer is stronger
- Character variety
-common patterns are not allowed
-entropy/score system: give some points based on the rules
"""
def length_check(password):
    password_length=len(password)
    if password_length>=12:
        return "Strong"
    elif password_length>=8:
        return "Medium"
    else:
        return "Weak (too short, use at least 8 characters)"

def variety_check(password):
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)
    if has_lower and has_upper and has_digit and has_symbol:
        return "Strong"
    else:
        return "Weak (use a mix of lowercase, uppercase, digits, and symbols)"
def common_patterns_check(password):
    if any(word in password for word in ["123456", "password","qwerty", "111111", "admin", "root", "letmein", "welcome", "iloveyou"]):
        return "Weak (avoid common patterns)"
    else:
        return "Strong"
def overall_strength(password: str) -> str:
    """Combine checks into an overall score."""
    results = [
        length_check(password),
        variety_check(password),
        common_patterns_check(password),
    ]

    score = 0
    for r in results:
        if r.startswith("Strong"):
            score += 2
        elif r.startswith("Medium"):
            score += 1
        # Weak = +0

    if score < 3:
        return "Weak"
    elif score < 5:
        return "Medium"
    return "Strong"