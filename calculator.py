import math

def square_root(x):
    """Calculates the square root of a number."""
    if x < 0:
        return "Error: Cannot calculate square root of a negative number."
    return math.sqrt(x)

def factorial(x):
    """Calculates the factorial of a non-negative integer."""
    if not isinstance(x, int) or x < 0:
        return "Error: Factorial is only defined for non-negative integers."
    return math.factorial(x)

def natural_log(x):
    """Calculates the natural logarithm (base e) of a number."""
    if x <= 0:
        return "Error: Natural logarithm is only defined for positive numbers."
    return math.log(x)

def power(base, exponent):
    """Calculates the power of a number."""
    return math.pow(base, exponent)

def display_menu():
    """Displays the calculator menu."""
    print("\n--- Scientific Calculator Menu ---")
    print("1. Square Root (√x)")
    print("2. Factorial (!x)")
    print("3. Natural Logarithm (ln(x))")
    print("4. Power (x^b)")
    print("5. Exit")
    print("---------------------------------")

def main():
    """Main function to run the calculator."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            try:
                num = float(input("Enter a number: "))
                print(f"Result: √{num} = {square_root(num)}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '2':
            try:
                num = int(input("Enter a non-negative integer: "))
                print(f"Result: {num}! = {factorial(num)}")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        elif choice == '3':
            try:
                num = float(input("Enter a positive number: "))
                print(f"Result: ln({num}) = {natural_log(num)}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            try:
                base = float(input("Enter the base (x): "))
                exp = float(input("Enter the exponent (b): "))
                print(f"Result: {base}^{exp} = {power(base, exp)}")
            except ValueError:
                print("Invalid input. Please enter numbers for base and exponent.")
        elif choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 5.")

if __name__ == "__main__":
    main()