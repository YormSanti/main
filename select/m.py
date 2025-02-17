import random
import string
import time

def addition():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Result: {num1 + num2}")

def subtraction():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Result: {num1 - num2}")

def multiplication():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Result: {num1 * num2}")

def division():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"Result: {num1 / num2}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

def string_reversal():
    string = input("Enter a string: ")
    print(f"Reversed string: {string[::-1]}")

def check_palindrome():
    string = input("Enter a string: ")
    if string == string[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

def count_vowels():
    string = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = sum(1 for char in string if char in vowels)
    print(f"Vowel count: {count}")

def generate_otp():
    otp = ''.join(random.choices(string.digits, k=6))
    print(f"Generated OTP: {otp}")

def generate_password():
    length = int(input("Enter password length: "))
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    print(f"Generated Password: {password}")

def get_current_datetime():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"Current date and time: {current_time}")

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Mathematical Operations")
        print("2. String Operations")
        print("3. Utility Functions")
        print("4. Exit")
        
        choice = input("Please select an option (1-4): ")
        
        if choice == "1":
            print("\nMathematical Operations:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            math_choice = input("Select an operation (1-4): ")
            if math_choice == "1":
                addition()
            elif math_choice == "2":
                subtraction()
            elif math_choice == "3":
                multiplication()
            elif math_choice == "4":
                division()
            else:
                print("Invalid choice. Returning to main menu.")
        
        elif choice == "2":
            print("\nString Operations:")
            print("1. String Reversal")
            print("2. Check Palindrome")
            print("3. Count Vowels")
            string_choice = input("Select an operation (1-3): ")
            if string_choice == "1":
                string_reversal()
            elif string_choice == "2":
                check_palindrome()
            elif string_choice == "3":
                count_vowels()
            else:
                print("Invalid choice. Returning to main menu.")
        
        elif choice == "3":
            print("\nUtility Functions:")
            print("1. Generate OTP")
            print("2. Generate Password")
            print("3. Get Current Date and Time")
            utility_choice = input("Select an operation (1-3): ")
            if utility_choice == "1":
                generate_otp()
            elif utility_choice == "2":
                generate_password()
            elif utility_choice == "3":
                get_current_datetime()
            else:
                print("Invalid choice. Returning to main menu.")
        
        elif choice == "4":
            print("Exiting the program...")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the menu
main_menu()
