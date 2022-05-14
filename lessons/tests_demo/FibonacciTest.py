import unittest
from main import fibonacci


class FibonacciTest(unittest.TestCase):

    def setUp(self):
        self.fib = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711

    def test_all(self):
        for i, f in enumerate(self.fib):
            self.assertEqual(fibonacci(i), f)


if __name__ == '__main__':
    unittest.main()
