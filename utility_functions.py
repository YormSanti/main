# utility_functions.py
import datetime
import random

def current_time():
    """Returns the current time."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def is_even(n):
    """Checks if a number is even."""
    return n % 2 == 0

def is_odd(n):
    """Checks if a number is odd."""
    return n % 2 != 0

def generate_random_number(start, end):
    """Generates a random number between start and end."""
    return random.randint(start, end)

def is_prime(n):
    """Checks if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    """Returns a list of the first n Fibonacci numbers."""
    fib_sequence = [0, 1]
    for _ in range(n - 2):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def otp_generator(length=6):
    """Generates a random one-time password (OTP) of the given length."""
    return "".join(str(random.randint(0, 9)) for _ in range(length))