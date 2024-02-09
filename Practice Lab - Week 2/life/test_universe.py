import unittest
from universe import Universe


class TestUniverse(unittest.TestCase):
    def test_generate(self):
        # Checking that method is correctly generating child classes.
        u1 = Universe()
        self.assertEqual(u1.generate(), True, "Output should be true.")

    def test_display(self):
        # Comparing intended output against expected output.
        u1 = Universe()
        self.assertEqual(u1.display(), None, "Output should be none.")