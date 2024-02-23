import unittest
from human import Human
from clothing import Clothing
from clothingsize import ClothingSize


class TestHuman(unittest.TestCase):

    def test_eat(self) -> None:
        # energy is full and try to eat
        human_joe = Human("joe")
        self.assertEqual(human_joe.eat(20), 20, "Excess should be 20.")

        # energy is below 100 and eat more than required
        human_joe = Human("joe", energy=90)
        self.assertEqual(human_joe.eat(20), 10, "Excess should 20.")

        # energy is below 100 and eat exactly what is required
        human_joe = Human("joe", energy=80)
        self.assertEqual(human_joe.eat(20), 0, "Excess should be 0.")

        # energy is below 100 and eat less than required
        human_joe = Human("joe", energy=70)
        self.assertEqual(human_joe.eat(20), -10, "Excess should be -10.")

    def test_grow(self) -> None:
        # Age increments appropriately
        human_joe = Human("joe", age=25)
        self.assertEqual(human_joe.grow(), 26, "Age should increment by 1.")

    def test_reproduce(self) -> None:
        # human has enough energy and can reproduce.
        human_joe = Human("joe", energy=40)
        self.assertEqual(human_joe.reproduce(), True, "Energy should decrease by 20.")

        # human does not have enough energy, they cannot reproduce.
        human_joe = Human("joe", energy=15)
        self.assertEqual(human_joe.reproduce(), False, "Energy should decrease by 20.")

    def test_move(self) -> None:
        # human has enough energy and can move.
        human_joe = Human("joe", energy=10)
        self.assertEqual(human_joe.move(1), True, "Energy should decrease by 20.")

        # human does not have enough energy, they cannot reproduce.
        human_joe = Human("joe", energy=10)
        self.assertEqual(human_joe.move(2), False, "Energy should decrease by 20.")

    def test_dress(self) -> None:
        # Tests that objects of the Clothing class can successfully be appended and removed from an instance array.
        human_test = Human("Jack")
        clothes_item = Clothing("red", "wool", ClothingSize(2))
        self.assertEqual(human_test.dress(clothes_item), True, "Should return True if successful.")
        self.assertEqual(human_test.undress(clothes_item), False, "Should return False if successful.")


if __name__ == '__main__':
    unittest.main()