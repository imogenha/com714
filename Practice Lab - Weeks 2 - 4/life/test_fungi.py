from fungi import Fungi
import unittest


class TestFungi(unittest.TestCase):

    def setUp(self):
        print("Running setUp method...")
        self.test_fungi_big = Fungi("mushroom", 1, 39, 1)
        self.test_fungi_small = Fungi("mushroom", 1, 39, 1)

    def tearDown(self):
        print("Running tearDown method...")

    def testSpread(self):
        # Checking output against expected results.
        self.assertEqual(self.test_fungi_big.spread(60), 61, "Increment should match expected output")
        # Ensuring correct error handling for negative numbers.
        self.assertEqual(self.test_fungi_small.spread(-2), 1, "Increment should match expected output")