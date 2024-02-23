import unittest
from venus_flytrap import VenusFlytrap


class TestFlytrap(unittest.TestCase):

    def setUp(self):
        print("Running setUp method...")
        self.flytrap_1 = VenusFlytrap("test1", 2, 40)
        self.flytrap_2 = VenusFlytrap("test2", 2, 40)

    def tearDown(self):
        print("Running tearDown method...")

    def test_catch(self):
        # Method output should change the value of the class instance of 'Colour'.
        self.assertEqual(self.flytrap_1.catch(3), 40 or 43, "Output should be a string.")

        self.assertEqual(self.flytrap_2.catch(-1), 40, "Output should be a string.")