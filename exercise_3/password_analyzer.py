

common_passwords = [
    "password123",
    "qwerty",
    "letmein",
    "dragonball",
    "baseball",
    "iloveyou",
    "monkey",
    "sunshine",
    "princess",
    "azerty",
    "qwertyuiop",
    "asdfghjkl",
    "123456",
    "12345678",
    "123456789",
    "1234567890",
    "abcdefg",
    "helloworld",
    "password",
    "admin"
]
def style1():
    print("\n")
    print("*" * 70)
def style2():
    print("\n")
    print("-" * 70)

def analyze_password(password):
    score = 0
    results = []

    # Check length requirement
    if len(password) >= 8:
        score += 20
        results.append("✅ Length requirement (8+ chars)")
    else:
        results.append("❌ Length requirement (8+ chars)")

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        score += 20
        results.append("✅ Contains uppercase letters")
    else:
        results.append("❌ Contains uppercase letters")

    # Check for lowercase letters
    if any(char.islower() for char in password):
        score += 20
        results.append("✅ Contains lowercase letters")
    else:
        results.append("❌ Contains lowercase letters")

    # Check for numbers
    if any(char.isdigit() for char in password):
        score += 20
        results.append("✅ Contains numbers")
    else:
        results.append("❌ Contains numbers")

    # Check for special characters
    if any(char in "!@#$%^&*" for char in password):
        score += 20
        results.append("✅ Contains special characters")
    else:
        results.append("❌ Contains special characters")

    # Check for common passwords
    if password in common_passwords:
        results.append("❌ Common password detected")
    else:
        score += 20
        results.append("✅ Not a common password")

    # Determine strength level
    if score <= 40:
        strength = "Weak"
    elif score <= 60:
        strength = "Fair"
    elif score <= 80:
        strength = "Good"
    elif score <= 100:
        strength = "Strong"
    else:
        strength = "Excellent"

    # Generate improvement suggestions
    suggestions = []
    if password in common_passwords:
        suggestions.append("- Avoid common password patterns")
    if len(password) < 8:
        suggestions.append("- Use a longer password")
    if not any(char.isupper() for char in password):
        suggestions.append("- Use uppercase letters")
    if not any(char.islower() for char in password):
        suggestions.append("- Use lowercase letters")
    if not any(char.isdigit() for char in password):
        suggestions.append("- Use numbers")
    if not any(char in "!@#$%^&*" for char in password):
        suggestions.append("- Use special characters")

    return {
        "password": password,
        "score": score,
        "strength": strength,
        "results": results,
        "suggestions": suggestions
    }


while True:
    style1()
    print("=== PASSWORD SECURITY ANALYZER ===")
    password = input("Enter Password please or type 'exit' to quit: ")
    if password.lower() == 'exit':
        style2()
        print(" Goodbye!")
        style2()
        break
    else:
        analysis =analyze_password(password)
        print(f"Password: {analysis['password']}")
        print(f"Score: {analysis['score']}/120 ({analysis['strength']})")
        for result in analysis["results"]:
            print(result)
        if analysis["suggestions"]:
            print("\n💡 SUGGESTIONS:")
            for suggestion in analysis["suggestions"]:
                print(suggestion)
        style1()




