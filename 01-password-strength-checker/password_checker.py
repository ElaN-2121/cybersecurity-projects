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
    if password_length>=8:
        return "Strong"
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
def entropy_check(password):
    score=0
    entropy=len(password)
    if entropy>=8:
        score+=2
    if entropy>=12:
        score+=2
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        score += 2
    if any(char.isdigit() for char in password):
        score += 2
    if any(char in string.punctuation for char in password):
        score += 2    
    if score < 4:
        return "Weak"
    elif score < 7:
        return "Medium"
    else:
        return "Strong"

def main():
    password=input("Enter your password: ")
    while True:
        print("Password Strength Checker: ")
        print("1. Length")
        print("2. Variety")
        print("3. Common Patterns")
        print("4. Entropy") 
        print("5. Change Password")
        print("6. Run All Checks")
        print("7. Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            print("Length check: ", length_check(password))
        elif choice==2:
            print("Variety check: ", variety_check(password))
        elif choice==3:
            print("Common patterns check: ", common_patterns_check(password))
        elif choice==4:
            print("Entropy check: ", entropy_check(password))
        elif choice == 5:
            password = input("Enter a new password: ")
        elif choice==6:
            length_result = length_check(password)
            variety_result = variety_check(password)
            pattern_result = common_patterns_check(password)
            entropy_result = entropy_check(password)
            results = [length_result, variety_result, pattern_result, entropy_result]

            score = 0
            for r in results:
                if r.startswith("Strong"):
                    score += 2
                elif r.startswith("Weak"):
                    score += 0
            def overall_check(score):
                if score < 4:
                    return "Weak"
                elif score < 7:
                    return "Medium"
                else:
                    return "Strong"
            print("\nPassword Strength Checker Results: ")
            print("Length check: ", length_result)
            print("Variety check: ", variety_result)
            print("Common patterns check: ", pattern_result)
            print("Entropy check: ", entropy_result)
            print("=========================================\n")
            print("\n=== Overall Password Strength: {} ===\n".format(overall_check(score)))
        elif choice==7:
            break
        else:
            print("Please insert a valid choice")
            choice=int(input("Enter your choice: "))
if __name__=="__main__":
    main()  
