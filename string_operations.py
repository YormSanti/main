def reverse_string(s):
    """Returns the reversed version of a string."""
    return s[::-1]

def capitalize_string(s):
    """Capitalizes the first letter of a string."""
    return s.capitalize()

def count_vowels(s):
    """Counts the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def count_consonants(s):
    """Counts the number of consonants in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char.isalpha() and char not in vowels)

def to_uppercase(s):
    """Converts a string to uppercase."""
    return s.upper()

def to_lowercase(s):
    """Converts a string to lowercase."""
    return s.lower()

def remove_whitespace(s):
    """Removes all whitespace from a string."""
    return "".join(s.split())

def is_palindrome(s):
    """
    Checks if a string is a palindrome.
    A palindrome is a word, phrase, or sequence that reads the same forward and backward.
    Example:
        - print(is_palindrome("madam"))  # ✅ True (palindrome)
        - print(is_palindrome("racecar"))  # ✅ True (palindrome)
        - print(is_palindrome("hello"))  # ❌ False (not a palindrome)
        - print(is_palindrome("12321"))  # ✅ True (palindrome)
        - print(is_palindrome("Python"))  # ❌ False (not a palindrome)
    """
    return s == s[::-1]