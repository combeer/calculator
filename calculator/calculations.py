# calculator/calculations.py

def add(a, b):
    """Compute and return the sum of two numbers.
    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0


    Args:
        a (float): A number representing the first addend in the addition.
        b (float): A number representing the second addend in the addition.

    Returns:
        float: A number representing the arithmetic sum of `a` and `b`.
    """
    return float(a + b)

	

def subtract(a, b):

    """Compute and return the difference of two numbers.
    Examples:
        >>> subtract(4.0, 2.0)
        2.0
        >>> subtract(4, 2)
        2.0


    Args:
        a (float): A number representing the first number.
        b (float): A number representing the second number.

    Returns:
        float: A number representing the arithmetic difference of `a` and `b`.
    """

    return float(a - b)

def multiply(a, b):
    """Compute and return the product of two numbers.

    Examples:
        >>> multiply(4.0, 2.0)
        8.0
        >>> multiply(4, 2)
        8.0


    Args:
        a (float): A number representing the first addend in the multiplication.
        b (float): A number representing the second addend in the multiplication.

    Returns:
        float: A number representing the product of `a` and `b`.
    """

    return float(a * b)

def divide(a, b):
    """Compute and return the quotient of two numbers.
    
    Examples:
        >>> divide(4.0, 2.0)
        2.0
        >>> divide(4, 2)
        2.0

    Args:
        a (float): A number representing the first dividend in the division.
        b (float): A number representing the second dividend in the division.

    Returns:
        float: A number representing the dividend of `a` and `b`.
    """

    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)

