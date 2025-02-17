import select.math_operations as math_ops
import select.string_operations as str_ops
import select.utility_functions as utils


def get_float_input(prompt):
    
    """Prompts the user for a floating-point number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_int_input(prompt):
    """Prompts the user for an integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main_menu():
    while True:
    
        print("\nMain Menu")
        print("1. Math Operations")
        print("2. String Operations")
        print("3. Utility Functions")
        print("4. Exit")
        choice = get_int_input("Enter your choice (1-4): ")
        if choice == 1:
            math_menu()
        elif choice == 2:
            string_menu()
        elif choice == 3:
            utility_menu()
        elif choice == 4:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def math_menu():
    while True:
        print("\nMath Operations Menu")
        print("1. add")
        print("2. subtract")
        print("3. multiply")
        print("4. divide")
        print("5. modulus")
        print("6. power")
        print("7. factorial")
        print("8. Back to Main Menu")
        
        choice = get_int_input("Enter your choice (1-8): ")

        if choice == 1:
            print("Addition")
            a = get_float_input("Enter the first number: ")
            b = get_float_input("Enter the second number: ")
            result = math_ops.add(a, b)
            print(f"The sum of {a} and {b} is: {result}")
        elif choice == 2:
            print("Subtraction")
            a = get_float_input("Enter the first number: ")
            b = get_float_input("Enter the second number: ")
            result = math_ops.subtract(a, b)
            print(f"The difference of {a} and {b} is: {result}")
        elif choice == 3:
            print("Multiplication")
            a = get_float_input("Enter the first number: ")
            b = get_float_input("Enter the second number: ")
            result = math_ops.multiply(a, b)
            print(f"The product of {a} and {b} is: {result}")
        elif choice == 4:
            print("Division")
            a = get_float_input("Enter the dividend: ")
            b = get_float_input("Enter the divisor: ")
            result = math_ops.divide(a, b)
            print(f"The quotient of {a} divided by {b} is: {result}")
        elif choice == 5:
            print("Modulus")
            a = get_float_input("Enter the dividend: ")
            b = get_float_input("Enter the divisor: ")
            result = math_ops.modulus(a, b)
            print(f"The remainder of {a} divided by {b} is: {result}")
        elif choice == 6:
            print("Power")
            a = get_float_input("Enter the base: ")
            b = get_float_input("Enter the exponent: ")
            result = math_ops.power(a, b)
            print(f"{a} raised to the power of {b} is: {result}")
        elif choice == 7:
            print("Factorial")
            n = get_int_input("Enter a non-negative integer: ")
            result = math_ops.factorial(n)
            print(f"The factorial of {n} is: {result}")
        elif choice == 8:
            break # Go back to the main menu
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

def string_menu():
    while True:
        print("\nString Operations Menu")
        print("1. reverse")
        print("2. capitalize")
        print("3. count_vowels")
        print("4. count_consonants")
        print("5. Back to Main Menu")
        
        
        choice = get_int_input("Enter your choice (1-5): ")

        if choice == 1:
            print("Reverse")
            s = input("Enter a string: ")
            result = str_ops.reverse(s)
            print(f"The reversed string is: {result}")
        elif choice == 2:
            print("Capitalize")
            s = input("Enter a string: ")
            result = str_ops.capitalize(s)
            print(f"The capitalized string is: {result}")
        elif choice == 3:
            print("Count Vowels")
            s = input("Enter a string: ")
            result = str_ops.count_vowels(s)
            print(f"The number of vowels in the string is: {result}")
        elif choice == 4:
            print("Count Consonants")
            s = input("Enter a string: ")
            result = str_ops.count_consonants(s)
            print(f"The number of consonants in the string is: {result}")
        elif choice == 5:
            break # Go back to the main menu
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def utility_menu():
    while True:
        print("\nUtility Functions Menu")
        print("1. current_time")
        print("2. is_even")
        print("3. is_odd")
        print("4. generate_random_number")
        print("5. is_prime")
        print("6. fibonacci")
        print("7. otp_generator")
        print("8. Back to Main Menu")
        
        choice = get_int_input("Enter your choice (1-8): ")

        if choice == 1:
            print("Current Time")
            result = utils.current_time()
            print(f"The current time is: {result}")
        elif choice == 2:
            print("Is Even")
            n = get_int_input("Enter a number: ")
            result = utils.is_even(n)
            print(f"{n} is {'even' if result else 'odd'}.")
        elif choice == 3:
            print("Is Odd")
            n = get_int_input("Enter a number: ")
            result = utils.is_odd(n)
            print(f"{n} is {'odd' if result else 'even'}.")
        elif choice == 4:
            print("Generate Random Number")
            start = get_int_input("Enter the start of the range: ")
            end = get_int_input("Enter the end of the range: ")
            result = utils.generate_random_number(start, end)
            print(f"A random number between {start} and {end} is: {result}")
        elif choice == 5:
            print("Is Prime")
            n = get_int_input("Enter a number: ")
            result = utils.is_prime(n)
            print(f"{n} is {'prime' if result else 'not prime'}.")
        elif choice == 6:
            print("Fibonacci")
            n = get_int_input("Enter the number of Fibonacci numbers to generate: ")
            result = utils.fibonacci(n)
            print(f"The first {n} Fibonacci numbers are: {result}")
        elif choice == 7:
            print("OTP Generator")
            length = get_int_input("Enter the length of the OTP: ")
            result = utils.otp_generator(length)
            print(f"The generated OTP is: {result}")
        elif choice == 8:
            break # Go back to the main menu
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

# Start the program
if __name__ == "__main__":
    main_menu()