import unittest
from clothing import Clothing
from clothingsize import ClothingSize


class TestClothing(unittest.TestCase):

    def setUp(self):
        print("Running setUp method...")
        self.clothing_item = Clothing("Green", "Wool", ClothingSize(2))
        self.test_item_small = Clothing("Green", "Wool", ClothingSize(1))
        self.test_item_big = Clothing("Green", "Wool", ClothingSize(5))

    def tearDown(self):
        print("Running tearDown method...")

    def test_dye(self):
        # Method output should change the value of the class instance of 'Colour'.
        self.assertEqual(self.clothing_item.dye("green"), True, "Output should be a string.")
        print(self.clothing_item.str())

    def test_grow(self) -> None:
        # Clothing enums increment in size, and illegal incrementation is appropriately handled.
        self.assertEqual(self.clothing_item.gain_weight(), ClothingSize(3), "Age should increment by 1.")

        self.assertEqual(self.test_item_big.gain_weight(), print("Cannot gain any more weight!"),
                         "Method should block attempts at creating illegal class instances.")

    def test_shrink(self) -> None:
        # Clothing enums decrement in size, and illegal decrementation is appropriately handled.
        self.assertEqual(self.clothing_item.loose_weight(), ClothingSize(1), "Age should increment by 1.")

        self.assertEqual(self.test_item_small.loose_weight(), print("Cannot lose any more weight!"),
                         "Method should block attempts at creating illegal class instances.")


if __name__ == '__main__':
    unittest.main()