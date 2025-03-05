from typing import List

def fibonacci(n: int) -> List[int]:
    """Generates the first n Fibonacci numbers."""
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    
    return sequence[:n]
