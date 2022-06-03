# Task 7.11
# Implement a generator which will generate Fibonacci numbers endlessly.

def endless_generator():
    """
    Yield Fibonacci numbers endlessly.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def main():
    generator = endless_generator()
    for _ in range(20):
        print(next(generator))
        
main() 
