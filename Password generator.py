import random
import string

def generate_password(length, complexity):
    if complexity == '1':  # Simple: only letters
        characters = string.ascii_letters
    elif complexity == '2':  # Medium: letters + digits
        characters = string.ascii_letters + string.digits
    elif complexity == '3':  # Strong: letters + digits + symbols
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity choice."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("=== 🔐 Password Generator ===")
try:
    length = int(input("Enter the desired password length: "))
    print("\nChoose complexity level:")
    print("1. Simple (letters only)")
    print("2. Medium (letters + digits)")
    print("3. Strong (letters + digits + symbols)")
    complexity = input("Enter your choice (1/2/3): ")

    password = generate_password(length, complexity)
    print(f"\nGenerated Password: {password}")
except ValueError:
    print("Please enter a valid number for password length.")
