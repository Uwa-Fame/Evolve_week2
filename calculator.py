
def add (a, b):
    """ A function that adds two numbers together

    Args:
    index(a) (int): A single lower case that represent the first number
    index(b) (int): A single lower case that represent the second number
   
    Returns:
    the addition of two numbers

    """
    return a + b


def subtract(a, b):
    
    """ A function that adds two numbers together

    Args:
    index(a) (int): A single lower case that represent the first number
    index(b) (int): A single lower case that represent the second number
   
    Returns:
    the difference of two number

    """
    return a - b
    

    
def multiply (a, b):
    """
    A function that returns the product of two numbers.
    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The product of the two numbers.
    """
    return a * b
    
# divide only if the number is greater than zero
def divide(a, b):
    """
    A function that divides a number if the number is greater than zero.
    Args:
        a (int): the first number
        b (int): the second number
   
    Returns:
    the difference of two numbers 
"""
    
    if b == 0:
        return "cannot devide by zero"
    return a / b

# main section
print(f" 3 + 4 = {add(3, 4)}")
print(f" 4 - 3 = {subtract(4, 3)}")
print(f"12 * 3 = {multiply(12, 3)}")
print(f"20 / 5 = {divide(20, 5)}")

