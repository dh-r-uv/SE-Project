import math

class CalculatorError(Exception):
    pass

def sqrt(x):
    if x < 0:
        raise CalculatorError("Cannot compute square root of a negative number.")
    return math.sqrt(x)

def fact(x):
    if not isinstance(x, int) or x < 0:
        raise CalculatorError("Factorial is only defined for non-negative integers.")
    return math.factorial(x)

def log(x):
    if x <= 0:
        raise CalculatorError("Natural logarithm is only defined for positive numbers.")
    return math.log(x)

def power(base, exponent):
    return math.pow(base, exponent)

def display_menu():
    print("change")
    print("\nCalculator Menu ")
    print("1. Square Root (√x)")
    print("2. Factorial (x!)")
    print("3. Logorithm (ln(x))")
    print("4. Power (x^b)")
    print("5. Exit")

def main():
    while True:
        display_menu()
        option = input("Enter your option (1-5): ")
        if option == '1':
            try:
                num = float(input("Enter a number: "))
                print(f"Result: √{num} = {sqrt(num)}")
            except ValueError:
                print("Invalid input. Please enter a number.")
                
        elif option == '2':
            try:
                num = int(input("Enter a non-negative integer: "))
                print(f"Result: {num}! = {fact(num)}")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        elif option == '3':
            try:
                num = float(input("Enter a positive number: "))
                print(f"Result: ln({num}) = {log(num)}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif option == '4':
            try:
                base = float(input("Enter the base (x): "))
                exp = float(input("Enter the exponent (b): "))
                print(f"Result: {base}^{exp} = {power(base, exp)}")
            except ValueError:
                print("Invalid input. Please enter numbers for base and exponent.")
        elif option == '5':
            print("Exiting!")
            break
        else:
            print("Invalid option. Please select an option from 1 to 5.")

if __name__ == "__main__":
    main()