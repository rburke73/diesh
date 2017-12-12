from random import seed, randint
from unittest import TestCase

from dice.sides import dice


class SideTestCase(TestCase):
    def test_dice(self):
        seed(0)
        expected_roll = [randint(1, 6)]
        seed(0)
        self.assertEqual(list(expected_roll), dice(1, 6))