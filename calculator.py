
def add (a, b):
    return a + b

def subtract(a, b):
    return a - b

    
def multiply (a, b):
    return a * b
# divide only if the number is greater than zero
def divide(a, b):
    if b == 0:
        return "cannot devide by zero"
    return a / b

# main section
print(f" 3 + 4 = {add(3, 4)}")
print(f" 4 - 3 = {subtract(4, 3)}")
print(f"12 * 3 = {multiply(12, 3)}")
print(f"20 / 5 = {divide(20, 5)}")

