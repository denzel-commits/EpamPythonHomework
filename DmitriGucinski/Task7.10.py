# Task 7.10
# Implement a generator which will generate odd numbers endlessly.

def endless_generator():
    """ Yield odd numbers endlessly. """
    value = 1
    while True:
        yield value
        value += 2


def main():
    for i in endless_generator():
        print(i)
        
main()        
