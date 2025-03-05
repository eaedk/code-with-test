class Calculator:
    """A simple calculator class with basic operations."""
    
    @staticmethod
    def add(a: float, b: float) -> float:
        """Returns the sum of a and b."""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Returns the difference of a and b."""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Returns the product of a and b."""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Returns the quotient of a and b. Raises ValueError if dividing by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
