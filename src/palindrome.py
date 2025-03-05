def is_palindrome(s: str) -> bool:
    """Checks if a string is a palindrome (ignores case and spaces)."""
    if len(s) > 1:
        cleaned = ''.join(c.lower() for c in s if c.isalnum())  # Remove spaces and special characters
        return cleaned == cleaned[::-1]
    else:
        return False
