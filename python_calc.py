def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: you can't divide by zero."
    return a / b


def even_or_odd(n):
    if n != int(n):
        return f"{n} is a decimal, so it is neither even nor odd."
    if int(n) % 2 == 0:
        return f"{int(n)} is even."
    return f"{int(n)} is odd."


def percentage(a, b):
    if b == 0:
        return "Error: the second number can't be zero."
    return f"{a} is {(a / b) * 100:.2f}% of {b}"


def get_number(prompt):
    # keeps asking until the user types a valid number
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a number, try again.")


def show_menu():
    print("\n===== Python Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Check Even/Odd")
    print("6. Calculate Percentage")
    print("7. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        if choice in ("1", "2", "3", "4"):
            a = get_number("Enter the first number: ")
            b = get_number("Enter the second number: ")
            if choice == "1":
                result = add(a, b)
            elif choice == "2":
                result = subtract(a, b)
            elif choice == "3":
                result = multiply(a, b)
            else:
                result = divide(a, b)
            print("Result:", result)

        elif choice == "5":
            n = get_number("Enter a number: ")
            print(even_or_odd(n))

        elif choice == "6":
            a = get_number("Enter the first number: ")
            b = get_number("Enter the second number: ")
            print(percentage(a, b))

        else:
            print("Invalid choice. Please pick a number from 1 to 7.")


main()
