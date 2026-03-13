"""
Basic Mathematical Operations Module

This module contains basic mathematical utility functions.
Students can contribute by implementing the functions marked with TODO comments.

Author: Student Contributors
Last Updated: February 2026
"""

from typing import Union


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def power(base: Union[int, float], exponent: int) -> Union[int, float]:
    if exponent == 0:
        return 1
    elif exponent > 0:
        result = 1
        for _ in range(exponent):
            result *= base
        return result
    else:
        # Handle negative exponents
        result = 1
        for _ in range(-exponent):
            result *= base
        return 1 / result


def square_root(number: Union[int, float], precision: float = 1e-10) -> float:
    """
    Calculate the square root of a number using Newton's method.
    
    This implements square root calculation without using built-in functions.
    
    Args:
        number (Union[int, float]): The number to find square root of
        precision (float): The desired precision (default: 1e-10)
        
    Returns:
        float: The square root of the number
        
    Raises:
        ValueError: If number is negative
        
    Examples:
        >>> square_root(16)
        4.0
        >>> square_root(2)  # approximately
        1.4142135623730951
    
    TODO: Implement this function
    Hint: Use Newton's method: x_new = (x + number/x) / 2
    """
    pass