import unittest

from demo.body_mass_index import bmi


class BmiTestCase(unittest.TestCase):

    @staticmethod
    def mass(idx, height):
        return idx * height ** 2

    def test_first(self):
        h = 172
        m = BmiTestCase.mass(10, h)
        idx, msg = bmi(h, m)
        self.assertEqual(idx, 10)
        self.assertEqual(msg, 'Выраженный дефицит массы тела')

    def test_second(self):
        h = 172
        m = BmiTestCase.mass(17, h)
        idx, msg = bmi(h, m)
        self.assertEqual(idx, 17)
        self.assertEqual(msg, 'Недостаточная(дефицит) масса тела')