import sys
def add():
    a = float(input("Enter the first value: "))
    b = float(input("Enter the second value: "))
    result = a + b
    print(f"Addition of {a} and {b} = {result}")
    return result

def sub():
    a = float(input("Enter the first value: "))
    b = float(input("Enter the second value: "))
    result = a - b
    print(f"Subtraction of {a} and {b} = {result}")
    return result

def mul():
    a = float(input("Enter the first value: "))
    b = float(input("Enter the second value: "))
    result = a * b
    print(f"Multiplication of {a} and {b} = {result}")
    return result

def div():
    a = float(input("Enter the first value: "))
    b = float(input("Enter the second value: "))
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    result = a / b
    print(f"Division of {a} and {b} = {result}")
    return result

def floordiv():
    a = float(input("Enter the first value: "))
    b = float(input("Enter the second value: "))
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    result = a // b
    print(f"Floor Division of {a} and {b} = {result}")
    return result

def per():
    a = float(input("Enter the first value: "))
    b = float(input("Enter the second value: "))
    result = (a % b)
    print(f"Remainder of {a} and {b} = {result}")
    return result


def calculator():
    print("-" * 50)
    print("\t\tSimple Calculator")
    print("-" * 50)
    print("\t\t 1. Addition  (+)")
    print("\t\t 2. Subtraction  (-)")
    print("\t\t 3. Multiplication  (*)")
    print("\t\t 4. Division (/)")
    print("\t\t 5. Floor Division (//)")
    print("\t\t 6. Remainder (%)")
    print("\t\t 7. Exit ")
    print("-" * 50)

    while True:
        try:
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    add()
                case 2:
                    sub()
                case 3:
                    mul()
                case 4:
                    div()
                case 5:
                    floordiv()
                case 6:
                    per()
                case 7:
                    print("Thanks for using the calculator. Goodbye!")
                    sys.exit()
                case _:
                    print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    calculator()
