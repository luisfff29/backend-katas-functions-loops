#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "luisfff29"

import operator


def add(x, y):
    """Add two integers. Handles negative values."""
    return x + y


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    if x == 0 or y == 0:
        return 0
    elif x == -1 or y == -1:
        return operator.neg(x) if y == -1 else operator.neg(y)
    elif x == 1 or y == 1:
        return x if y == 1 else y
    else:
        result = add(x, x)
        if y < 0:
            for i in range(operator.neg(y) - 2):
                result = add(result, x)
            return operator.neg(result)
        else:
            for i in range(y - 2):
                result = add(result, x)
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
    """Compute factorial of x, where x > 0"""  # x CAN be 0; 0! == 1
    if x < 0:
        return "x can't be 0 or a negative number"
    if x == 0 or x == 1:
        return 1
    else:
        result = multiply(x, x-1)
        for i in range(x-2, 0, -1):
            result = multiply(result, i)
        return result


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    if n == 1:
        return 0
    if n == 2 or n == 3:
        return 1
    else:
        (a, b) = (1, 1)
        result = add(a, b)
        for i in range(n-4):
            (result, b) = (b, result)
            result = add(result, b)
        return result


if __name__ == '__main__':
    """Calling the functions above"""
    print('add(2, 4) = ' + str(add(2, 4)))
    print('multiply(6, -8) = ' + str(multiply(6, -8)))
    print('power(2, 8) = ' + str(power(2, 8)))
    print('factorial(4) = ' + str(factorial(4)))
    print('fibonacci(8) = ' + str(fibonacci(8)))
