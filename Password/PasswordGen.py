import random

strong = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+=-{}[]:;\"'<>,.?/|~"
medium = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
easy = "abcdefghijklmnopqrstuvwxyz0123456789"

def generate():
    print("Choose password Complexcity:")
    print("1. High (includes letters, numbers, and special characters)")
    print("2. Medium (includes letters and numbers)")
    print("3. Low (includes lowercase letters and numbers only)")

    choice = input("Enter your choice (1, 2, or 3): ").strip()

    if choice == '1':
        characters = strong
    elif choice == '2':
        characters = medium
    elif choice == '3':
        characters = easy
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        return

    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be a positive number.")
            return
    except ValueError:
        print("Invalid input. Please enter a numeric value for the password length.")
        return


    password = ''.join(random.choice(characters) for _ in range(length))
    strength = 'Strong' if choice == '1' else 'Medium' if choice == '2' else 'Easy'
    print(f"Generated Password ({strength}): {password}")

generate()
