import unittest
from universe import Universe


class TestUniverse(unittest.TestCase):
    def test_generate_entity(self):
        # Checking that method is correctly generating child classes.
        u1 = Universe()
        self.assertEqual(u1.generate_entity(['E1', 'E2']), True, "Output should be true.")

    def test_generate_planet(self):
        # Checking that method is correctly generating child classes.
        u1 = Universe()
        self.assertEqual(u1.generate_entity(['P1', 'P2']), True, "Output should be true.")

    def test_display_entity(self):
        # Comparing intended output against expected output.
        u1 = Universe()
        self.assertEqual(u1.display_entity(), None, "Output should be none.")

    def test_display_nonplanet(self):
        # Comparing intended output against expected output.
        u1 = Universe()
        self.assertEqual(u1.display_nonplanet(), None, "Output should be none.")