import unittest
from universe import Universe


class TestUniverse(unittest.TestCase):
    def test_generate(self):
        # Checking that method is correctly generating child classes.
        u1 = Universe()
        self.assertEqual(u1.generate(), True, "Output should be true.")

    def test_display_planet(self):
        # Comparing intended output against expected output.
        u1 = Universe()
        self.assertEqual(u1.display_planet(), None, "Output should be none.")

    def test_display_nonplanet(self):
        # Comparing intended output against expected output.
        u1 = Universe()
        self.assertEqual(u1.display_nonplanet(), None, "Output should be none.")