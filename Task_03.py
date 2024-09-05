import re

def check_password_strength(password):
    # Define criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[@$!%*?&]', password) is not None

    # Determine password strength
    score = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        number_criteria,
        special_char_criteria
    ])

    # Feedback on password strength
    if score == 5:
        strength = "Very Strong"
        feedback = "Your password meets all the criteria. Excellent job!"
    elif score == 4:
        strength = "Strong"
        feedback = "Your password is strong but could be improved."
    elif score == 3:
        strength = "Moderate"
        feedback = "Your password is moderate. Consider adding more complexity."
    elif score == 2:
        strength = "Weak"
        feedback = "Your password is weak. Please add more complexity."
    else:
        strength = "Very Weak"
        feedback = "Your password does not meet the minimum criteria. Please choose a stronger password."

    return strength, feedback

def main():
    # Get password input from user
    password = input("Enter your password: ")

    # Check password strength
    strength, feedback = check_password_strength(password)

    # Print results
    print(f"Password Strength: {strength}")
    print(feedback)

if __name__ == "__main__":
    main()
