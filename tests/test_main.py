#!/usr/bin/env python

import unittest
import math
import random
import main


class TestMain(unittest.TestCase):

    def test_add(self):
        self.assertIsNotNone(main.add)
        for _ in range(10):
            x = random.randrange(-1000, 1000)
            y = random.randrange(-1000, 1000)
            self.assertEqual(main.add(x, y), x + y)

    def test_multiply(self):
        self.assertIsNotNone(main.multiply)
        self.assertEqual(main.multiply(-2, -3), 6)
        self.assertEqual(main.multiply(-2, 3), -6)
        self.assertEqual(main.multiply(2, -3), -6)
        self.assertEqual(main.multiply(2, 3), 6)
        for _ in range(10):
            x = random.randrange(-1000, 1000)
            y = random.randrange(-1000, 1000)
            self.assertEqual(main.multiply(x, y), x * y)

    def test_power(self):
        self.assertIsNotNone(main.power)
        self.assertEqual(main.power(3, 4), 3 ** 4)
        self.assertEqual(main.power(-2, 3), -2 ** 3)
        self.assertEqual(main.power(62, 0), 1)
        for _ in range(10):
            x = random.randrange(-10, 10)
            y = random.randrange(0, 10)
            self.assertEqual(main.power(x, y), x ** y)

    def test_factorial(self):
        self.assertIsNotNone(main.factorial)
        self.assertEqual(main.factorial(4), math.factorial(4))
        for x in range(10):
            self.assertEqual(main.factorial(x), math.factorial(x))

    def test_fibonacci(self):
        self.assertIsNotNone(main.fibonacci)
        fibs = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
        for n in range(1, 11):
            self.assertEqual(main.fibonacci(n), fibs[n-1])
            # should be fibs[n-1] beucase on the README.d file says:
            # Display the result of calling fibonacci(8), which should be 13:

            # 0 1 1 2 3 5 8 [13] 21

            # The number in brackets is the 8th fibonacci number.
            # >>>
            # 8th position wich it means on the index 7.
            # With that argument we can say:
            # 0 is in the 1st position
            # 1 is in the 2nd position
            # 1 is in the 3rd position
            # 2 is in the 4th position
            # and so on...


if __name__ == '__main__':
    unittest.main()
