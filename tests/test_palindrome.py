from src.palindrome import is_palindrome

def test_true_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("12321") is True

def test_false_palindrome():
    assert is_palindrome("hello") is False
    assert is_palindrome("Not a palindrome") is False
    
    
def test_min_length_palindrome():    
    assert is_palindrome("a") is False
    assert is_palindrome("") is False
