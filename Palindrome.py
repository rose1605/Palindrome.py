import re
def is_palindrome(s: str) -> bool:
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    # Check if the cleaned string is equal to its reverse
    return cleaned_s == cleaned_s[::-1]


# Example usage
print(is_palindrome("madam"))  # Should return True
print(is_palindrome("racecar"))  # Should return True
print(is_palindrome("hello"))  # Should return False
print(is_palindrome("A man, a plan, a canal, Panama!"))  # Should return True