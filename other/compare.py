def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1


def is_between(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False
        
def factorial(n):  # silnia
    if n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        return result

def fibonacci(n):
    if not isinstance(n, int):
        print("Factorial is only defined for integers.")
        return None
    elif n < 0:
        print("Factorial is not defined for negative numbers.")
        return None
    elif n == 0:
        return 0
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        return result
