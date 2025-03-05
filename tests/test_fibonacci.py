import pytest

from src.fibonacci import fibonacci

def test_fibonacci():
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_invalid():
    with pytest.raises(ValueError, match="n must be a positive integer."):
        fibonacci(0)
