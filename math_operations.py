def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the quotient of two numbers."""
    if b == 0:
        return "Error! Division by zero."
    return a / b

def modulus(a, b):
    """Returns the modulus of two numbers (remainder of division)."""
    return a % b

def power(base, exponent):
    """Returns the base raised to the power of exponent."""
    return base ** exponent

def factorial(n):
    """Returns the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)