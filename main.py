#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "luisfff29"


def add(x, y):
    """Add two integers. Handles negative values."""
    return x + y


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    if x == 0 or y == 0:
        return 0
    elif x == 1 or y == 1:
        return x if y == 1 else y
    elif x == -1 or y == -1:
        return -x if y == -1 else -y
    else:
        result = add(x, x)
        for i in range(abs(y)-2):
            result = add(result, x)
        if y < 0:
            return -result
        else:
            return result


def power(x, n):
    """Raise x to power n, where n >= 0"""
    if n < 0:
        return "n can't be a negative number"
    elif n == 0 or x == 0:
        return 0 if x == 0 else 1
    elif n == 1:
        return x
    else:
        result = multiply(x, x)
        for i in range(n - 2):
            result = multiply(result, x)
        return result


def factorial(x):
    """Compute factorial of x, where x > 0"""
    if x <= 0:
        return "x can't be 0 or a negative number"
    if x == 1:
        return x
    else:
        result = multiply(x, x-1)
        for i in range(x-2, 0, -1):
            result = multiply(result, i)
        return result


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    # your code here
    return


if __name__ == '__main__':
    # your code to call functions above
    pass
